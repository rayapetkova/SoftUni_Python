prime_sum = 0
non_prime_sum = 0

while True:
    digit = input()

    if digit == "stop":
        break

    digit = int(digit)
    if digit < 0:
        print(f"Number is negative.")
        continue

    counter = 0

    for i in range(2, digit + 1):
        if digit % i == 0:
            counter += 1

    if counter == 1:
        prime_sum = prime_sum + digit
    else:
        non_prime_sum = non_prime_sum + digit

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")