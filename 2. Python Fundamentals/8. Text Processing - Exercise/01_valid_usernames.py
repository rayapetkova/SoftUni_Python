usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        not_valid = False
        for el in username:
            if not el.isalpha() and not el.isdigit() and el != "-" and el != "_":
                not_valid = True
                break
        if not not_valid:
            print(username)




#2
#
# usernames = input().split(", ")
#
# for username in usernames:
#     if 3 <= len(username) <= 16:
#
#         for el in username:
#             if not el.isalpha() and not el.isdigit() and el != "-" and el != "_":
#                 break
#         else:
#             print(username)
