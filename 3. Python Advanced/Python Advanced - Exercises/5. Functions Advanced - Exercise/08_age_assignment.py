def age_assignment(*args, **kwargs):
    final = []

    for first_letter in kwargs.keys():
        for name in args:

            if name.startswith(first_letter):
                final.append(f"{name} is {kwargs[first_letter]} years old.")

    sorted_final = list(sorted(final))

    return "\n".join(sorted_final)


# Test inputs:
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
