all_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while True:
    movie_name = input()

    if movie_name == "Finish":
        print(f"Total tickets: {all_tickets}")

        student_tickets_percents = (student_tickets / all_tickets) * 100
        print(f"{student_tickets_percents:.2f}% student tickets.")

        standard_tickets_percents = (standard_tickets / all_tickets) * 100
        print(f"{standard_tickets_percents:.2f}% standard tickets.")

        kid_tickets_percents = (kid_tickets / all_tickets) * 100
        print(f"{kid_tickets_percents:.2f}% kids tickets.")
        break

    free_seats = int(input())
    counter_seats = 0
    while True:
        type_ticket = input()

        if type_ticket == "End":
            break
        counter_seats = counter_seats + 1
        all_tickets = all_tickets + 1

        if type_ticket == "student":
            student_tickets = student_tickets + 1
        elif type_ticket == "standard":
            standard_tickets = standard_tickets + 1
        elif type_ticket == "kid":
            kid_tickets = kid_tickets + 1
        if counter_seats == free_seats:
            break

    percents_taken_seats = (counter_seats / free_seats) * 100
    print(f"{movie_name} - {percents_taken_seats:.2f}% full.")