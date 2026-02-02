import csv
from typing import List
from datetime import datetime

CVS_FIlE_PATH = './TaskD/week42.csv'

# Läser in CSV
def read_csv_file(file_path: str) -> None:
    data = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            data.append(row)
    print_data(data)


# Skriver ut data
def print_data(data: List) -> None:
    #header = data[0]
    print("Week 42 electricity consumption and production")
    print("-" * 68)
    print(f"{'Date':<18} "f"{'Consumption [kWh]':<24} {'Production [kWh]':<20}")
    print(f"{'(dd.mm.yyyy)':<6} "
          f"{'v1':>7}{'v2':>8}{'v3':>8} "
          f"{'v1':>8}{'v2':>8}{'v3':>8}")
    print("-" * 68)

    for row in data[1:]:
        dt = datetime.fromisoformat(row[0])
        date_key = dt.strftime("%d.%m.%Y")
        cons_v1 = to_kwh(float(row[1]))
        cons_v2 = to_kwh(float(row[2]))
        cons_v3 = to_kwh(float(row[3]))
        prod_v1 = to_kwh(float(row[4]))
        prod_v2 = to_kwh(float(row[5]))
        prod_v3 = to_kwh(float(row[6]))
        print(f"{date_key:<12} "
              f"{format_kwh(cons_v1):>8}{format_kwh(cons_v2):>8}{format_kwh(cons_v3):>8} "
              f"{format_kwh(prod_v1):>8}{format_kwh(prod_v2):>8}{format_kwh(prod_v3):>8}")
 

# Huvudfunktion
def main() -> None:
    read_csv_file(CVS_FIlE_PATH)


def to_kwh(wh: float) -> float:
    return wh / 1000.0

def format_kwh(value_kwh: float) -> str:
    return f"{value_kwh:.2f}".replace(".", ",")


# Kör huvudfunktionen
if __name__ == "__main__":
    main()