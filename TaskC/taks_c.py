# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
A program that prints reservation information according to task requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime

HEADERS = [
    "reservationId",
    "name",
    "email",
    "phone",
    "reservationDate",
    "reservationTime",
    "durationHours",
    "price",
    "confirmed",
    "reservedResource",
    "createdAt",
]


def convert_reservation_data(reservation: list) -> list:
    reservation = [x.strip() for x in reservation]

    reservation_id = int(reservation[0])
    name = reservation[1]
    email = reservation[2]
    phone = reservation[3]

    reservation_date = datetime.strptime(reservation[4], "%Y-%m-%d").date()

    time_str = reservation[5]
    time_format = "%H:%M:%S" if time_str.count(":") == 2 else "%H:%M"
    reservation_time = datetime.strptime(time_str, time_format).time()

    duration_hours = int(reservation[6])
    price = float(reservation[7])
    confirmed = reservation[8] == "True"
    reserved_resource = reservation[9]
    created_at = datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id,
        name,
        email,
        phone,
        reservation_date,
        reservation_time,
        duration_hours,
        price,
        confirmed,
        reserved_resource,
        created_at,
    ]


def fetch_reservations(reservation_file: str) -> list:
    """
    Reads reservations from a file and returns the reservations converted
    You don't need to modify this function!

    Parameters:
     reservation_file (str): Name of the file containing the reservations

    Returns:
     reservations (list): Read and converted reservations
    """
    reservations = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.split("|")
            reservations.append(convert_reservation_data(fields))
    return reservations


def confirmed_reservations(reservations: list[list]) -> None:
    for r in reservations:
        if r[8]:
            name = r[1]
            resource = r[9]
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {name}, {resource}, {date_str} at {time_str}")


def long_reservations(reservations: list[list]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list): Reservations
    """
    for r in reservations:
        if r[6] >= 3:
            name = r[1]
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            duration = r[6]
            resource = r[9]
            print(f"- {name}, {date_str} at {time_str}, duration {duration} h, {resource}")


def confirmation_statuses(reservations: list[list]) -> None:
       for r in reservations:
        name = r[1]
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{name} \u2192 {status}")



def confirmation_summary(reservations: list[list]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (list): Reservations
    """
    confirmed_count = 0
    not_confirmed_count = 0

    for r in reservations:
        if r[8]:
            confirmed_count += 1
        else:
            not_confirmed_count += 1

    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")


def total_revenue(reservations: list[list]) -> None:
    total = 0.0
    for r in reservations:
        if r[8]:
            total += r[6] * r[7]

    amount_str = f"{total:.2f}".replace(".", ",")
    print(f"Total revenue from confirmed reservations: {amount_str} €")


def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations("reservations.txt")
    # PART A -> Before continuing to part B, make sure that the following lines
    # print all the reservation data and the correct data types to the console. 
    # After that, you can remove this section or comment it out up to part B.
    print(" | ".join(HEADERS))
    print("------------------------------------------------------------------------")
    for reservation in reservations:
        print(" | ".join(str(x) for x in reservation))
        data_types = [type(x).__name__ for x in reservation]
        print(" | ".join(data_types))
        print(
            "------------------------------------------------------------------------"
        )

    # PART B -> Build the output required in part B from this using
    # the predefined functions and the necessary print statements.

    #print("1) Confirmed Reservations")
    # confirmed_reservations(reservations)
    # Continue from here
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print()

    print("2) Long Reservations (\u2265 3 h)")
    long_reservations(reservations)
    print()

    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print()

    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print()

    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)


if __name__ == "__main__":
    main()