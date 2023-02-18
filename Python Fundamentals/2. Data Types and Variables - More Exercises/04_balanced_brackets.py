n = int(input())
example = ""
not_balanced = False

for i in range(1, n + 1):
    text = input()
    if text != "(" and text != ")":
        continue
    if text == "(" and example == "":
        example += "("
    elif text == ")" and example == "(":
        example = ""
    else:
        not_balanced = True
        break

if not not_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")