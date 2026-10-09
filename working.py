import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # 9:00 AM to 5:00 PM ----> 09:00 to 17:00
    # 12:30 AM to 8:50 AM ----> 00:30 to 08:50
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE)
    if time:

        # ValueErrors
        if time.group(2) and int(time.group(2)) >= 60:
            raise ValueError

        if time.group(5) and int(time.group(5)) >= 60:
            raise ValueError

        # time1
        hour1 = int(time.group(1))
        if time.group(3) == "PM" and hour1 != 12:
            hour1 += 12
        elif time.group(3) == "AM" and hour1 == 12:
            hour1 -= 12

        minute1 = time.group(2) if time.group(2) else "00"
        time1 = f"{hour1:02}:{minute1}"

        # time2
        hour2 = int(time.group(4))
        if time.group(6) == "PM" and hour2 !=12:
            hour2 += 12
        elif time.group(6) == "AM" and hour2 == 12:
            hour2 -= 12

        minute2 = time.group(5) if time.group(5) else "00"
        time2 = f"{hour2:02}:{minute2}"

        # return in 24-hour format
        time = f"{time1} to {time2}"
        return time

    else:
        raise ValueError


if __name__ == "__main__":
    main()
