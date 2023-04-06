days = int(input())

doctors = 7
treated_people = 0
untreated_people = 0

for i in range(1, days + 1):
    patients = int(input())
    if i % 3 == 0 and untreated_people > treated_people:
        doctors = doctors + 1
    if patients == doctors:
        treated_people = treated_people + doctors
    elif patients < doctors:
        treated_people = treated_people + patients
    elif patients > doctors:
        treated_people = treated_people + doctors
        untreated_people = untreated_people + (patients - doctors)

print(f"Treated patients: {treated_people}.")
print(f"Untreated patients: {untreated_people}.")