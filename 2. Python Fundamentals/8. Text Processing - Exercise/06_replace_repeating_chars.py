text = input()
new = ""

for element in text:
    if len(new) > 0:
        if element not in new[-1]:
            new += element
    else:
        new += element

print(new)
