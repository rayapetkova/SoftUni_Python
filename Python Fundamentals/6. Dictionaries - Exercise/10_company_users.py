from collections import OrderedDict

companies = {}

while True:
    line = input()
    if line == "End":
        break
    company_name, company_id = line.split(" -> ")
    companies[company_name] = companies.get(company_name, []) + [company_id]

for name, all_id in companies.items():
    print(name)
    for id in list(OrderedDict.fromkeys(all_id)):
        print(f"-- {id}")