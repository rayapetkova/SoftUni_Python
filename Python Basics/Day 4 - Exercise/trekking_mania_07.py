count_groups = int(input())

people_Musala = 0
people_Montblanc = 0
people_Kilimanjaro = 0
people_K2 = 0
people_Everest = 0
all_people = 0

for i in range(1, count_groups + 1):
    people = int(input())

    if people <= 5:
        people_Musala = people_Musala + people
    elif 6 <= people <= 12:
        people_Montblanc = people_Montblanc + people
    elif 13 <= people <= 25:
        people_Kilimanjaro = people_Kilimanjaro + people
    elif 26 <= people <= 40:
        people_K2 = people_K2 + people
    elif people >= 41:
        people_Everest = people_Everest + people

all_people = people_Musala + people_Montblanc + people_Kilimanjaro + people_K2 + people_Everest

percents_Musala = (people_Musala / all_people) * 100
print(f"{percents_Musala:.2f}%")

percents_Montblanc = (people_Montblanc / all_people) * 100
print(f"{percents_Montblanc:.2f}%")

percents_Kilimanjaro = (people_Kilimanjaro / all_people) * 100
print(f"{percents_Kilimanjaro:.2f}%")

percents_K2 = (people_K2 / all_people) * 100
print(f"{percents_K2:.2f}%")

percents_Everest = (people_Everest / all_people) * 100
print(f"{percents_Everest:.2f}%")