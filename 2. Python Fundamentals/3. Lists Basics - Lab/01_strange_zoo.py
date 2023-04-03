tail = input()
body = input()
head = input()
strange_animal = [tail, body, head]

strange_animal[0], strange_animal[2] = strange_animal[2], strange_animal[0]

print(strange_animal)