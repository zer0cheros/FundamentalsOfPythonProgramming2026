from datetime import datetime

_RESERVATIONS = "reservations.txt"

def print_reservation_number(r):
    print(f"Reservation number: {r['id']}")

def print_booker(r):
    print(f"Booker: {r['name']}")

def print_date(r):
    print(f"Date: {r['date'].strftime('%d.%m.%Y')}")

def print_start_time(r):

    print(f"Start time: {r['start'].strftime('%H.%M')}")

def print_hours(r):
    print(f"Number of hours: {r['hours']}")

def print_hourly_rate(r):
    print(f"Hourly price: {r['price']:.2f} €".replace(".", ","))

def print_total_price(r):
    total = r["hours"] * r["price"]
    print(f"Total price: {total:.2f} €".replace(".", ","))

def print_paid(r):
    print(f"Paid: {'Yes' if r['paid'] else 'No'}")

def print_venue(r):
    print(f"Location: {r['room']}")

def print_phone(r):
    print(f"Phone: {r['phone']}")

def print_email(r):
    print(f"Email: {r['email']}")

def main():
    with open(_RESERVATIONS, encoding="utf-8") as f:
        reservation_id, name, date, start, hours, price, paid, room, phone, email = (
            f.read().strip().split("|")
        )

    reservation = {
        "id": int(reservation_id),
        "name": name.strip(),
        "date": datetime.strptime(date.strip(), "%Y-%m-%d").date(),
        "start": datetime.strptime(start.strip(), "%H:%M").time(),  # convert to time
        "hours": float(hours.strip()),
        "price": float(price.strip()),
        "paid": paid.strip() == "True",
        "room": room.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
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
