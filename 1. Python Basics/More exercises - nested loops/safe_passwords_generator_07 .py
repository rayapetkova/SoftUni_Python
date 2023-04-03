a = int(input())
b = int(input())
max_num_passwords = int(input())

counter = 0
for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                counter = counter + 1
                if counter > max_num_passwords:
                    exit()
                    break

                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

                if x == a and y == b:
                    exit()
                    break
                A = A + 1
                B = B + 1
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64