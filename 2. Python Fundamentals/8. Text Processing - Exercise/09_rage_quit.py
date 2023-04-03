text = input()
result, used, final = "", "", ""

for element in range(len(text)):
    if not text[element].isdigit():
        result += text[element]
    else:
        if element + 1 < len(text) and text[element + 1].isdigit():
            number = int(text[element] + text[element + 1])
            used += str(number)
        elif text[element] in used and text[element] == used[-1]:
            used = ""
            continue
        else:
            number = int(text[element])
        final += (result * number).upper()
        result = ""

print(f"Unique symbols used: {len(set(final))}\n{final}")