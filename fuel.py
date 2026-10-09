while True:
    num = input("Fraction: ")
    index = num.find("/")
    try:
        x = int(num[:index])
        y = int(num[index+1:])
        fraction = x / y
        if x > y:
            continue
        break
    except (ValueError, ZeroDivisionError):
        continue

percentage = int(fraction * 100)

if percentage >= 99:
        print("F")
elif percentage <= 1:
        print("E")
else:
        print(str(percentage) + "%")
