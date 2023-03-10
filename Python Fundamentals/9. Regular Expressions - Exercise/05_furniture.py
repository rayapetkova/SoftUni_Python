import re

pattern = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
all_furniture_informations = ""
total = 0

while True:
    information = input()
    if information == "Purchase":
        break
    all_furniture_informations += information

valid_informations = re.finditer(pattern, all_furniture_informations)

print(f"Bought furniture:")
for valid_information in valid_informations:
    print(valid_information["furniture"])
    total += float(valid_information["price"]) * int(valid_information["quantity"])

print(f"Total money spend: {total:.2f}")