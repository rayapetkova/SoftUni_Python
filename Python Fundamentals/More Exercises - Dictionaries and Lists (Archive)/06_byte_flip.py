text = input().split()
elements = []
final = ""

for element in text:
    if len(element) == 2:
        elements.append(element)

for i in range(len(elements)):
    final += bytes.fromhex(elements[i][::-1]).decode("ASCII")

print(final[::-1])
