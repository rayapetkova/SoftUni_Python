text = input().split()

new = ""

for word in text:
    new += word * len(word)

print(new)