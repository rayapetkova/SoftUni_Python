year = int(input()) + 1
string_year = str(year)

while len(set(string_year)) != len(string_year):
    year += 1
    string_year = str(year)

print(year)