
_RESERVAIONS = "reservations.txt"

def print_reservation_number(r):
    print(f"Reservation number: {r['id']}")

def print_booker(r):
    print(f"Booker: {r['name']}")

def print_date(r):
    print(f"Date: {r['date'].replace('-', '.')}")

def print_start_time(r):
    print(f"Start time: {r['start'].replace(':', '.')}")

def print_hours(r):
    print(f"Number of hours: {r['hours']}")

def print_hourly_rate(r):
    print(f"Hourly price: {r['price'].replace('.', ',')} €")

def print_total_price(r):
    total = float(r["hours"]) * float(r["price"])
    print(f"Total price: {str(total).replace('.', ',')} €")

def print_paid(r):
    print(f"Paid: {'Yes' if r['paid'] == 'True' else 'No'}")

def print_venue(r):
    print(f"Location: {r['room']}")

def print_phone(r):
    print(f"Phone: {r['phone']}")

def print_email(r):
    print(f"Email: {r['email']}")


def main():
    with open(_RESERVAIONS, encoding="utf-8") as r:
        reservation, name, date, start, hours, price, paid, room, phone, email = \
            r.read().strip().split("|")

    reservation = {
        "id": reservation,
        "name": name,
        "date": date,
        "start": start,
        "hours": hours,
        "price": price,
        "paid": paid,
        "room": room,
        "phone": phone,
        "email": email,
    }

    printers = [
        print_reservation_number,
        print_booker,
        print_date,
        print_start_time,
        print_hours,
        print_hourly_rate,
        print_total_price,
        print_paid,
        print_venue,
        print_phone,
        print_email,
    ]

    for printer in printers:
        printer(reservation)


if __name__ == "__main__":
    main()