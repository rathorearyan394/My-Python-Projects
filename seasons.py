from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")

    print(minutes_lived(year, month, day))

def minutes_lived(year, month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"
    today = date.today()
    diff = today - dt
    minutes = int(diff.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()
