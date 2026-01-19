
_RESERVAIONS = "reservations.txt"

def main():
    with open(_RESERVAIONS, 'r', encoding="utf-8") as r:
        texts = r.read().split('|')
        reservation, name, date, start, hours, price, paid, room, phone, email = texts
        total = float(hours) * float(price)

        print(f"Reservation number: {reservation}")
        print(f"Booker: {name}")
        print(f"Date: {date.replace('-', '.')}")
        print(f"Start time: {start.replace(':', '.')}")
        print(f"Number of hours: {hours}")
        print(f"Hourly price: {price.replace('.', ',')} €")
        print(f"Total price: {str(total).replace('.', ',')} €")
        print(f"Paid: {'Yes' if paid == 'True' else 'No'}")
        print(f"Location: {room}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print()
        

if __name__ == "__main__":
    main()