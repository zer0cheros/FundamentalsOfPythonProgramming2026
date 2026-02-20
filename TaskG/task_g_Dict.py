
# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
A program that prints reservation information according to requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime
import pathlib

path = pathlib.Path(__file__).parent

def convert_reservation_data(reservation: list) -> dict:
    """
    Convert data types to meet program requirements

    Parameters:
     reservation (list): Unconverted reservation -> 11 columns 

    Returns:
     converted (list): Converted data types
    """
    return {
    "id": int(reservation[0]),
    "name": reservation[1].strip(),
    "email": reservation[2].strip(),
    "phone": reservation[3].strip(),
    "date": datetime.strptime(reservation[4].strip(), "%Y-%m-%d").date(),
    "time": datetime.strptime(reservation[5].strip(), "%H:%M:%S").time()
    if ":" in reservation[5].strip() and len(reservation[5].strip().split(":")) == 3
    else datetime.strptime(reservation[5].strip(), "%H:%M").time(),
    "duration": int(reservation[6]),
    "price": float(reservation[7]),
    "confirmed": True if reservation[8].strip() == "True" else False,
    "resource": reservation[9].strip(),
    "created": datetime.strptime(reservation[10].strip(), "%Y-%m-%d %H:%M:%S"),
}


def fetch_reservations(reservation_file: str) -> list[dict]:
    """
    Reads reservations from a file and returns the reservations converted
    You don't need to modify this function!

    Parameters:
     reservation_file (str): Name of the file containing the reservations

    Returns:
     reservations (list): Read and converted reservations
    """
    reservations: list[dict] = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            fields = line.split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations

def confirmed_reservations(reservations: list[dict]) -> None:
    """
    Print confirmed reservations

    Parameters:
     reservations (list): Reservations
    """
    for r in reservations:
        if r["confirmed"]:
            print(
                f'- {r["name"]}, {r["resource"]}, {r["date"].strftime("%d.%m.%Y")} at {r["time"].strftime("%H.%M")}'
            )

def long_reservations(reservations : list[dict]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list): Reservations
    """
    for r in reservations:
        if r["duration"] > 3: # If long
           print(
                f'- {r["name"]}, {r["date"].strftime("%d.%m.%Y")} at {r["time"].strftime("%H.%M")}, '
                f'duration {r["duration"]} h, {r["resource"]}'
            )


def confirmation_statuses(reservations: list[list]) -> None:
    """
    Print confirmation statuses

    Parameters:
     reservations (list): Reservations
    """
    for r in reservations:
        name: str = r["name"]
        confirmed: bool = r["confirmed"]
        print(f'{name} → {"Confirmed" if confirmed else "NOT Confirmed"}')

def confirmation_summary(reservations: list[list]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (list): Reservations
    """
    for r in reservations:
        name: str = r["name"]
        confirmed: bool = r["confirmed"]
        print(f'{name} → {"Confirmed" if confirmed else "NOT Confirmed"}')

def total_revenue(reservations: list[list]) -> None:
    """
    Print total revenue

    Parameters:
     reservations (list): Reservations
    """
    revenue = sum(r["duration"] * r["price"] for r in reservations if r["confirmed"])
    print(f'Total revenue from confirmed reservations: {revenue:.2f} €'.replace(".", ","))

def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations(path / "reservations.txt")
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)

if __name__ == "__main__":
    main()
