# Copyright (c) 2025 Christian Wiss
# License: MIT

import csv
from datetime import datetime, date
from typing import List, Dict, Any
from helpers import format_date, format_number, month_name, parse_timestamp, path



DATE_FMT = "%d.%m.%Y"


def read_data(filename: str) -> List[Dict[str, Any]]:
    """Reads 2025.csv and returns rows with converted datatypes."""
    rows: List[Dict[str, Any]] = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for r in reader:
            # Adjust these keys if your CSV headers differ:
            ts = parse_timestamp(r["Time"])
            consumption = float(r[" Consumption (net) kWh"].replace(",", "."))
            production = float(r[" Production (net) kWh"].replace(",", "."))
            temp = float(r[" Daily average temperature"].replace(",", "."))

            rows.append({
                "dt": ts,
                "day": ts.date(),
                "consumption": consumption,
                "production": production,
                "temp": temp
            })
    return rows


def show_main_menu() -> str:
    """Shows the main menu and returns the user's choice."""
    print("\nChoose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit the program")
    return input("Select (1–4): ").strip()


def show_next_menu() -> str:
    """Shows the post-report menu and returns the user's choice."""
    print("\nWhat would you like to do next?")
    print("1) Write the report to the file report.txt")
    print("2) Create a new report")
    print("3) Exit")
    return input("Select (1–3): ").strip()


def ask_date(prompt: str) -> date:
    """Asks the user for a date in dd.mm.yyyy format and returns a date object."""
    while True:
        s = input(prompt).strip()
        try:
            return datetime.strptime(s, DATE_FMT).date()
        except ValueError:
            print("Invalid date format. Use dd.mm.yyyy (e.g., 13.10.2025).")


def ask_month() -> int:
    """Asks the user for a month number 1–12 and returns it."""
    while True:
        s = input("Enter month number (1–12): ").strip()
        if s.isdigit():
            m = int(s)
            if 1 <= m <= 12:
                return m
        print("Invalid month. Enter a number from 1 to 12.")


def create_daily_report(data: List[Dict[str, Any]]) -> List[str]:
    """Builds a report for a selected date range (inclusive)."""
    start = ask_date("Enter start date (dd.mm.yyyy): ")
    end = ask_date("Enter end date (dd.mm.yyyy): ")

    if end < start:
        start, end = end, start

    total_c = 0.0
    total_p = 0.0
    temp_sum = 0.0
    count = 0

    for row in data:
        if start <= row["day"] <= end:
            total_c += row["consumption"]
            total_p += row["production"]
            temp_sum += row["temp"]
            count += 1

    avg_temp = (temp_sum / count) if count > 0 else 0.0

    return [
        "-" * 53,
        f"Report for the period {format_date(start)}–{format_date(end)}",
        f"- Total consumption: {format_number(total_c)} kWh",
        f"- Total production: {format_number(total_p)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C",
    ]


def create_monthly_report(data: List[Dict[str, Any]]) -> List[str]:
    """Builds a monthly summary report for a selected month (1–12)."""
    m = ask_month()

    total_c = 0.0
    total_p = 0.0
    temp_sum = 0.0
    count = 0

    for row in data:
        if row["dt"].month == m:
            total_c += row["consumption"]
            total_p += row["production"]
            temp_sum += row["temp"]
            count += 1

    avg_temp = (temp_sum / count) if count > 0 else 0.0

    return [
        "-" * 53,
        f"Report for the month: {month_name(m)}",
        f"- Total consumption: {format_number(total_c)} kWh",
        f"- Total production: {format_number(total_p)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C",
    ]


def create_yearly_report(data: List[Dict[str, Any]]) -> List[str]:
    """Builds a full-year summary report for 2025."""
    total_c = 0.0
    total_p = 0.0
    temp_sum = 0.0
    count = 0

    for row in data:
        total_c += row["consumption"]
        total_p += row["production"]
        temp_sum += row["temp"]
        count += 1

    avg_temp = (temp_sum / count) if count > 0 else 0.0

    return [
        "-" * 53,
        "Report for the year: 2025",
        f"- Total consumption: {format_number(total_c)} kWh",
        f"- Total production: {format_number(total_p)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C",
    ]


def print_report_to_console(lines: List[str]) -> None:
    """Prints report lines to the console."""
    print("\n".join(lines))


def write_report_to_file(lines: List[str]) -> None:
    """Writes report lines to report.txt (overwrites old content)."""
    with open("report.txt", mode="w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    data = read_data(path / "2025.csv")

    while True:
        choice = show_main_menu()
        if choice == "4":
            break

        if choice == "1":
            report = create_daily_report(data)
        elif choice == "2":
            report = create_monthly_report(data)
        elif choice == "3":
            report = create_yearly_report(data)
        else:
            print("Invalid selection. Try again.")
            continue

        print_report_to_console(report)

        while True:
            next_choice = show_next_menu()
            if next_choice == "1":
                write_report_to_file(report)
                print("Report written to report.txt (overwritten).")
            elif next_choice == "2":
                break
            elif next_choice == "3":
                return
            else:
                print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()