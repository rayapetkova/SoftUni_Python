tickets = input().split()

def check(first, second, symbol):
    total_first = 0
    first_list = []
    for i in range(len(first)):
        if first[i] == symbol:
            total_first += 1
            if i == len(first) - 1:
                first_list.append(total_first)
        else:
            first_list.append(total_first)
            total_first = 0

    total_second = 0
    second_list = []
    for i in range(len(second)):
        if second[i] == symbol:
            total_second += 1
            if i == len(second) - 1:
                second_list.append(total_second)
        else:
            second_list.append(total_second)
            total_second = 0

    max_first = max(first_list)
    max_second = max(second_list)
    if max_first < max_second:
        return f'ticket "{first + second}" - {max_first}{symbol}'
    else:
        return f'ticket "{first + second}" - {max_second}{symbol}'


for ticket in tickets:
    if "," in ticket:
        ticket = ticket.replace(",", "")
    if ticket == "":
        continue
    half = int(len(ticket) / 2)
    if len(ticket) == 20:
        first_half = ticket[0:half]
        second_half = ticket[half:len(ticket)]
        if "@" * 20 in ticket or "#" * 20 in ticket or "$" * 20 in ticket or "^" * 20 in ticket:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        elif "@" * 6 in first_half and "@" * 6 in second_half:
            curr_symbol = "@"
            print(check(first_half, second_half, curr_symbol))
        elif "#" * 6 in first_half and "#" * 6 in second_half:
            curr_symbol = "#"
            print(check(first_half, second_half, curr_symbol))
        elif "$" * 6 in first_half and "$" * 6 in second_half:
            curr_symbol = "$"
            print(check(first_half, second_half, curr_symbol))
        elif "^" * 6 in first_half and "^" * 6 in second_half:
            curr_symbol = "^"
            print(check(first_half, second_half, curr_symbol))
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f"invalid ticket")
