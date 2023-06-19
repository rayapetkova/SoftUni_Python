def naughty_or_nice_list(lst, *args, **kwargs):
    dictionary = {
        'Nice': [],
        'Naughty': [],
        'Not found': []
    }

    for arg in args:
        current_names = []
        result = arg.split("-")
        counting_num, type_kid = result[0], result[1]
        for number, name in lst:
            if counting_num == str(number):
                current_names.append(name)
        if len(current_names) == 1:
            current_name = "".join(current_names)
            dictionary[type_kid].append(current_name)
            lst.remove((int(counting_num), current_name))

    if kwargs:
        for key, value in kwargs.items():
            all_kids = []
            for number, name in lst:
                if name == key:
                    all_kids.append(f"{number}-{name}")
            if len(all_kids) == 1:
                current_kid_info = "".join(all_kids)
                kid_name = current_kid_info[current_kid_info.index("-") + 1:]
                number = int(current_kid_info[:current_kid_info.index("-")])
                dictionary[value].append(kid_name)
                lst.remove((number, kid_name))

    for left_kid in lst:
        name = left_kid[1]
        dictionary['Not found'].append(name)

    final = []
    for k, v in dictionary.items():
        if v:
            final.append(f"{k}: {', '.join(kid_name for kid_name in v)}")

    return "\n".join(final)


# Test inputs:

# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))


# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))


# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
