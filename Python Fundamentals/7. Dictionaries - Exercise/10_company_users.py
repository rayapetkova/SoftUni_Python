companies = {}

while True:
    line = input()
    if line == "End":
        break
    company_name, company_id = line.split(" -> ")
    companies[company_name] = companies.get(company_name, [])
    if company_id not in companies[company_name]:
        companies[company_name].append(company_id)

for name, all_id in companies.items():
    print(name)
    for id in all_id:
        print(f"-- {id}")




#2
#
# from collections import OrderedDict
#
# companies = {}
#
# while True:
#     line = input()
#     if line == "End":
#         break
#     company_name, company_id = line.split(" -> ")
#     companies[company_name] = companies.get(company_name, []) + [company_id]
#
# for name, all_id in companies.items():
#     print(name)
#     for id in list(OrderedDict.fromkeys(all_id)):
#         print(f"-- {id}")
