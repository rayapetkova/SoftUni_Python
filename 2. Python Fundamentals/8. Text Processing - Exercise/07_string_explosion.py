text = input()
final = ""
explosion = 0

for i in range(len(text)):
    if text[i] == ">":
        explosion += int(text[i + 1])
        final += text[i]
        continue
    elif explosion > 0:
        explosion -= 1
        continue
    final += text[i]

print(final)
