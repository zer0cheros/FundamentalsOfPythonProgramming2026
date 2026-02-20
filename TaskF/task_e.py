# Copyright (c) 2026 Christian Wiss
# License: MIT


import csv
from helpers import path, mainMenu, underHeaders, months, DATE_COL, AMOUNT_COL, PRODUCT_COL, AVERAGE_TEMP
from datetime import datetime, date


DATE_FMT = "%d.%m.%Y"

def convert_time(time_str: str) -> datetime:
    """Converts either dd.mm.yyyy or ISO timestamp into datetime."""
    
    # If string contains "T", it's ISO format from CSV
    if "T" in time_str:
        return datetime.fromisoformat(time_str)
    return datetime.strptime(time_str, DATE_FMT)



CSV_FILE = path / "2025.csv"

def read_data(filename: str) -> list:
    """Reads a CSV file and returns the rows in a suitable structure."""
    with open (filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)   

def show_main_menu() -> str:
    """Prints the main menu and returns the user selection as a string."""
    print("Choose a report type:")
    while True:
        for item in mainMenu:
            print(f"{item['id']}. {item['content']}")
        selection = input("")
        if(selection == "4"):
            break
        else:
            for items2 in underHeaders:
                print(f"{items2['id']}. {items2['content']}")
            selection2 = input("")
            if(selection == "1" and selection2 == "1"): create_daily_report(read_data(CSV_FILE))
            if(selection == "2" and selection2 == "1"): create_monthly_report(read_data(CSV_FILE))
            if(selection == "3" and selection2 == "1"): create_yearly_report(read_data(CSV_FILE))   
            elif(selection2 == "2"):
                show_main_menu()
            elif(selection2 == "3"):
                break
            else:
                print("Invalid selection, please try again.")

        


def create_daily_report(data: list) -> list[str]:
    """Builds a daily report for a selected date range."""
    print("Enter start date (dd.mm.yyyy): ")
    selectStart = input("").strip()
    print("Enter end date (dd.mm.yyyy): ")
    selectEnd = input("").strip()
    start, end  = convert_time(selectStart).date(), convert_time(selectEnd).date()
    filtered = []
    average, totals, production = 0.0, 0.0, 0.0
    daysTotal = end - start
    print(daysTotal.days + 1)
    for row in data:
        row_date = convert_time(row[DATE_COL]).date()
        row_amount = float(row[AMOUNT_COL].replace(",", "."))
        row_average = float(row[AVERAGE_TEMP].replace(",", "."))
        row_production = float(row[PRODUCT_COL].replace(",", "."))
        if start <= row_date <= end:
            filtered.append((row_date, row_amount, row_average))
            average = average + row_average
            totals = totals + row_amount
            production = production + row_production
    filtered.sort(key=lambda x: x[0])
    average = (average / filtered.__len__()).__round__(2)
    totals = totals.__round__(2)
    report_lines = [
        "-" * 53,
        f"Report for the period {start}–{end}",
        f"- Total consumption: {totals} kWh",
        f"- Total production: {production} kWh",
        f"- Average temperature: {average} °C",
    ]
    print_report_to_console(report_lines)
    write_report_to_file(report_lines)
    #
                   
   

def create_monthly_report(data: list) -> list[str]:
    """Builds a monthly summary report for a selected month."""
    print("Enter month number (1–12): ")
    selectMonth = input("").strip()
    month = int(selectMonth)
    filtered = [] 
    average, totals, production = 0.0, 0.0, 0.0
    for row in data:
        row_date = convert_time(row[DATE_COL])
        row_amount = float(row[AMOUNT_COL].replace(",", "."))
        row_average = float(row[AVERAGE_TEMP].replace(",", "."))
        row_production = float(row[PRODUCT_COL].replace(",", "."))
        if row_date.month == month:
            filtered.append((row_date, row_amount, row_average))
            average = average + row_average
            totals = totals + row_amount
            production = production + row_production
    filtered.sort(key=lambda x: x[0])
    average = (average / filtered.__len__()).__round__(2)
    totals = totals.__round__(2)
    report_lines = [
        "-" * 53,
        f"Report for {months[month-1]['content']}",
        f"- Total consumption: {totals} kWh",
        f"- Total production: {production} kWh",
        f"- Average temperature: {average} °C",
    ]
    print_report_to_console(report_lines)
    write_report_to_file(report_lines)

def create_yearly_report(data: list) -> list[str]:
    """Builds a full-year summary report."""
    filtered = []
    average, totals, production = 0.0, 0.0, 0.0
    for row in data:
        row_amount = float(row[AMOUNT_COL].replace(",", "."))
        row_average = float(row[AVERAGE_TEMP].replace(",", "."))
        row_production = float(row[PRODUCT_COL].replace(",", "."))
        row_date = convert_time(row[DATE_COL])
        filtered.append((row_date, row_amount, row_average, row_production))
        average = average + row_average
        totals = totals + row_amount
        production = production + row_production
    filtered.sort(key=lambda x: x[0])
    average = (average / filtered.__len__()).__round__(2)
    totals = totals.__round__(2)
    production = production.__round__(2)
    report_lines = [
        "-" * 53,
        f"Report for the year 2025",
        f"- Total consumption: {totals} kWh",
        f"- Total production: {production} kWh",
        f"- Average temperature: {average} °C",
    ]
    print_report_to_console(report_lines)
    write_report_to_file(report_lines)

def print_report_to_console(lines: list[str]) -> None:
    """Prints report lines to the console."""
    print("\n".join(lines))

def write_report_to_file(lines: list[str]) -> None:
    """Writes report lines to the file report.txt."""
    with open("report.txt", mode="w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    

def main() -> None:
    """Main function: reads data, shows menus, and controls report generation."""
    show_main_menu()


if __name__ == "__main__":
    main()