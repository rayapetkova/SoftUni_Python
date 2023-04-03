hour = int(input())
day = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day =="Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
elif day == "Sunday":
    print("closed")