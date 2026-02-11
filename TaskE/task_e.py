import csv
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Totals:
    """Holds daily totals for consumption and production in kWh for phases v1–v3."""
    cons: Tuple[float, float, float]
    prod: Tuple[float, float, float]


def read_data(filename: str) -> List[List[str]]:
    """Reads a semicolon-separated CSV file and returns all rows (including header)."""
    rows: List[List[str]] = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row:  # skip completely empty lines
                rows.append(row)
    return rows


def to_kwh(wh: float) -> float:
    """Converts watt-hours (Wh) to kilowatt-hours (kWh)."""
    return wh / 1000.0


def format_kwh(value_kwh: float) -> str:
    """Formats a kWh value with two decimals and Finnish comma decimal separator."""
    return f"{value_kwh:.2f}".replace(".", ",")


def format_fi_date(d: date) -> str:
    """Formats a date as dd.mm.yyyy."""
    return d.strftime("%d.%m.%Y")


def weekday_fi(d: date) -> str:
    """Returns the weekday name in Finnish for the given date."""
    names = ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"]
    return names[d.weekday()]


def calculate_daily_summaries(rows: List[List[str]]) -> Dict[date, Totals]:
    """
    Calculates daily totals (kWh) for consumption and production by phase.

    Expects rows where:
      col0 = ISO timestamp (e.g. 2025-10-13T00:00:00)
      col1-3 = consumption phases v1-v3 in Wh
      col4-6 = production phases v1-v3 in Wh
    Returns: mapping date -> Totals(cons=(v1,v2,v3), prod=(v1,v2,v3)) in kWh.
    """
    daily_wh: Dict[date, List[float]] = {}  # [c1,c2,c3,p1,p2,p3] in Wh

    for row in rows[1:]:  # skip header
        dt = datetime.fromisoformat(row[0])
        day = dt.date()

        # Parse Wh values
        c1, c2, c3 = float(row[1]), float(row[2]), float(row[3])
        p1, p2, p3 = float(row[4]), float(row[5]), float(row[6])

        if day not in daily_wh:
            daily_wh[day] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        daily_wh[day][0] += c1
        daily_wh[day][1] += c2
        daily_wh[day][2] += c3
        daily_wh[day][3] += p1
        daily_wh[day][4] += p2
        daily_wh[day][5] += p3

    # Convert to kWh Totals
    daily_kwh: Dict[date, Totals] = {}
    for day, vals in daily_wh.items():
        cons = (to_kwh(vals[0]), to_kwh(vals[1]), to_kwh(vals[2]))
        prod = (to_kwh(vals[3]), to_kwh(vals[4]), to_kwh(vals[5]))
        daily_kwh[day] = Totals(cons=cons, prod=prod)

    return daily_kwh


def format_week_section(week_number: int, daily: Dict[date, Totals]) -> str:
    """
    Formats one week's daily totals as a report section.
    Days are output in chronological order.
    """
    lines: List[str] = []
    lines.append(f"Week {week_number} electricity consumption and production (kWh, by phase)")
    lines.append("Day          Date           Consumption [kWh]                 Production [kWh]")
    lines.append("                          v1       v2       v3              v1       v2       v3")
    lines.append("-" * 83)

    for day in sorted(daily.keys()):
        t = daily[day]
        line = (
            f"{weekday_fi(day):<12}  "
            f"{format_fi_date(day):<12}  "
            f"{format_kwh(t.cons[0]):>8} {format_kwh(t.cons[1]):>8} {format_kwh(t.cons[2]):>8}     "
            f"{format_kwh(t.prod[0]):>8} {format_kwh(t.prod[1]):>8} {format_kwh(t.prod[2]):>8}"
        )
        lines.append(line)

    lines.append("")  # blank line between weeks
    return "\n".join(lines)


def write_report(filename: str, content: str) -> None:
    """Writes the given report content to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    """Main function: reads week files, computes summaries, and writes summary.txt."""
    week_files = [
        (41, "week41.csv"),
        (42, "week42.csv"),
        (43, "week43.csv"),
    ]

    sections: List[str] = []
    grand_cons = [0.0, 0.0, 0.0]
    grand_prod = [0.0, 0.0, 0.0]

    for week_no, path in week_files:
        rows = read_data(path)
        daily = calculate_daily_summaries(rows)

        # accumulate grand totals (bonus)
        for totals in daily.values():
            for i in range(3):
                grand_cons[i] += totals.cons[i]
                grand_prod[i] += totals.prod[i]

        sections.append(format_week_section(week_no, daily))

    # Optional combined summary
    sections.append("All weeks combined totals (kWh)")
    sections.append("-" * 83)
    sections.append(
        "Consumption total (v1 v2 v3): "
        f"{format_kwh(grand_cons[0])}  {format_kwh(grand_cons[1])}  {format_kwh(grand_cons[2])}"
    )
    sections.append(
        "Production total (v1 v2 v3):  "
        f"{format_kwh(grand_prod[0])}  {format_kwh(grand_prod[1])}  {format_kwh(grand_prod[2])}"
    )
    sections.append("")

    report = "\n".join(sections)
    write_report("summary.txt", report)


if __name__ == "__main__":
    main()