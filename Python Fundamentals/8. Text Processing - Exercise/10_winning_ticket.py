tickets = input().split()


def adding_to_list(half, curr_symbol):
    total = 0
    half_symbols = []
    for i in range(len(half)):
        if half[i] == curr_symbol:
            total += 1
            if i == len(half) - 1:
                half_symbols.append(total)
        else:
            half_symbols.append(total)
            total = 0
    return max(half_symbols)


def final_result(first, second, symbol):
    max_first, max_second = adding_to_list(first, symbol), adding_to_list(second, symbol)
    if adding_to_list(first, symbol) < adding_to_list(second, symbol):
        return f'ticket "{first + second}" - {max_first}{symbol}'
    return f'ticket "{first + second}" - {max_second}{symbol}'


for ticket in tickets:
    ticket = ticket.replace(",", "")
    half = int(len(ticket) / 2)
    if ticket == "":
        continue
    if len(ticket) == 20:
        first_half = ticket[:half]
        second_half = ticket[half:]
        if any(["@" * 20 in ticket, "#" * 20 in ticket, "$" * 20 in ticket, "^" * 20 in ticket]):
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        elif all(["@" * 6 in first_half, "@" * 6 in second_half]):
            print(final_result(first_half, second_half, "@"))
        elif all(["#" * 6 in first_half, "#" * 6 in second_half]):
            print(final_result(first_half, second_half, "#"))
        elif all(["$" * 6 in first_half, "$" * 6 in second_half]):
            print(final_result(first_half, second_half, "$"))
        elif all(["^" * 6 in first_half, "^" * 6 in second_half]):
            print(final_result(first_half, second_half, "^"))
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f"invalid ticket")






#2
#
# tickets = input().split()
# symbols = {'at_symbol': ("@" * 6), 'pound_symbol': ("#" * 6), 'dollar_symbol': ("$" * 6), 'circumflex_symbol': ("^" * 6)}
#
#
# def adding_to_list(half, curr_symbol):
#     total = 0
#     half_symbols = []
#     for i in range(len(half)):
#         if half[i] == curr_symbol:
#             total += 1
#             if i == len(half) - 1:
#                 half_symbols.append(total)
#         else:
#             half_symbols.append(total)
#             total = 0
#     return max(half_symbols)
#
#
# def final_result(first, second, symbol):
#     max_first, max_second = adding_to_list(first, symbol), adding_to_list(second, symbol)
#     if adding_to_list(first, symbol) < adding_to_list(second, symbol):
#         return f'ticket "{first + second}" - {max_first}{symbol}'
#     return f'ticket "{first + second}" - {max_second}{symbol}'
#
#
# for ticket in tickets:
#     ticket = ticket.replace(",", "")
#     half = int(len(ticket) / 2)
#     if ticket == "":
#         continue
#     if len(ticket) == 20:
#         first_half = ticket[:half]
#         second_half = ticket[half:]
#         if any(["@" * 20 in ticket, "#" * 20 in ticket, "$" * 20 in ticket, "^" * 20 in ticket]):
#             print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
#         elif all([symbols['at_symbol'] in first_half, symbols['at_symbol'] in second_half]):
#             print(final_result(first_half, second_half, "@"))
#         elif all([symbols['pound_symbol'] in first_half, symbols['pound_symbol'] in second_half]):
#             print(final_result(first_half, second_half, "#"))
#         elif all([symbols['dollar_symbol'] in first_half, symbols['dollar_symbol'] in second_half]):
#             print(final_result(first_half, second_half, "$"))
#         elif all([symbols['circumflex_symbol'] in first_half, symbols['circumflex_symbol'] in second_half]):
#             print(final_result(first_half, second_half, "^"))
#         else:
#             print(f'ticket "{ticket}" - no match')
#     else:
#         print(f"invalid ticket")
