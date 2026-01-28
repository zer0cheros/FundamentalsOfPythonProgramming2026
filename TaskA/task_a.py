from datetime import datetime
_RESERVATIONS = "reservations.txt"

def main():
    with open(_RESERVATIONS, 'r', encoding="utf-8") as r:
        texts = r.read().strip().split('|')
        reservation = int(texts[0])
        name = texts[1].strip()
        date = datetime.strptime(texts[2].strip(), "%Y-%m-%d").date()
        start = datetime.strptime(texts[3].strip(), "%H:%M").time()
        hours = float(texts[4])
        price = float(texts[5])
        paid = texts[6].strip() == "True"
        room = texts[7].strip()
        phone = texts[8].strip()
        email = texts[9].strip()

        total = hours * price

        print(f"Reservation number: {reservation}")
        print(f"Booker: {name}")
        print(f"Date: {date}")
        print(f"Start time: {start}")
        print(f"Number of hours: {hours}")
        print(f"Hourly price: {price:.2f} €".replace('.', ','))
        print(f"Total price: {total:.2f} €".replace('.', ','))
        print(f"Paid: {'Yes' if paid else 'No'}")
        print(f"Location: {room}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print()

if __name__ == "__main__":
    main()
