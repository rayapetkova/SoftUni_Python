count_tabs = int(input())
salary = float(input())

salary1 = salary

for i in range(1, count_tabs + 1):
    website = input()
    if website == "Facebook":
        salary1 = salary1 - 150
    elif website == "Instagram":
        salary1 = salary1 - 100
    elif website == "Reddit":
        salary1 = salary1 - 50
    if salary1 <= 0:
        break

if salary1 <= 0:
    print(f"You have lost your salary.")
else:
    print(f"{salary1:.0f}")