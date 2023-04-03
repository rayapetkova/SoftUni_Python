number = int(input())
prime = False
counter = 0

for i in range(2, number):
    if number % i == 0:
        counter += 1

if counter == 0:
    prime = True

if prime:
    print("True")
else:
    print("False")