# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, date, time
import pathlib


path = pathlib.Path(__file__).parent


@dataclass
class Reservation:
    reservation_id: int
    name: str
    email: str
    phone: str
    date: date
    time: time
    duration: int
    price: float
    confirmed: bool
    resource: str
    created: datetime

    def is_confirmed(self) -> bool:
        return self.confirmed

    def is_long(self) -> bool:
        
        return self.duration > 3

    def total_price(self) -> float:
        return self.duration * self.price


def convert_reservation(data: list[str]) -> Reservation:
    """
    Convert one reservation row (list of 11 strings) into a Reservation object.
    """
    time_str = data[5].strip()
    parsed_time = (
        datetime.strptime(time_str, "%H:%M:%S").time()
        if ":" in time_str and len(time_str.split(":")) == 3
        else datetime.strptime(time_str, "%H:%M").time()
    )

    return Reservation(
        reservation_id=int(data[0]),
        name=data[1].strip(),
        email=data[2].strip(),
        phone=data[3].strip(),
        date=datetime.strptime(data[4].strip(), "%Y-%m-%d").date(),
        time=parsed_time,
        duration=int(data[6]),
        price=float(data[7]),
        confirmed=True if data[8].strip() == "True" else False,
        resource=data[9].strip(),
        created=datetime.strptime(data[10].strip(), "%Y-%m-%d %H:%M:%S"),
    )


def fetch_reservations(reservation_file: str) -> list[Reservation]:
    """
    Reads reservations from a file and returns converted reservations as objects.
    Does NOT include a header row.
    """
    reservations: list[Reservation] = []
    with open(reservation_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            fields = line.split("|")
            reservations.append(convert_reservation(fields))
    return reservations


def confirmed_reservations(reservations: list[Reservation]) -> None:
    for r in reservations:
        if r.is_confirmed():
            print(
                f'- {r.name}, {r.resource}, {r.date.strftime("%d.%m.%Y")} at {r.time.strftime("%H.%M")}'
            )


def long_reservations(reservations: list[Reservation]) -> None:
    for r in reservations:
        if r.is_long():
            print(
                f'- {r.name}, {r.date.strftime("%d.%m.%Y")} at {r.time.strftime("%H.%M")}, '
                f'duration {r.duration} h, {r.resource}'
            )


def confirmation_statuses(reservations: list[Reservation]) -> None:
    for r in reservations:
        print(f'{r.name} → {"Confirmed" if r.confirmed else "NOT Confirmed"}')


def confirmation_summary(reservations: list[Reservation]) -> None:
    confirmed_count = sum(1 for r in reservations if r.is_confirmed())
    not_confirmed_count = len(reservations) - confirmed_count
    print(
        f"- Confirmed reservations: {confirmed_count} pcs\n"
        f"- Not confirmed reservations: {not_confirmed_count} pcs"
    )


def total_revenue(reservations: list[Reservation]) -> None:
    revenue = sum(r.total_price() for r in reservations if r.is_confirmed())
    print(f'Total revenue from confirmed reservations: {revenue:.2f} €'.replace(".", ","))


def main() -> None:
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
