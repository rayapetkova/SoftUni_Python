first_line = input().split()
second_line = input().split()
third_line = input().split()

counter1_1 = 0
counter2_1 = 0

counter1_2 = 0
counter2_2 = 0

counter1_3 = 0
counter2_3 = 0

first_player_won = False
second_player_won = False

# diagonals:

if (first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1") or \
        (first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1"):
    first_player_won = True
    print("First player won")
    exit()
elif (first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2") or \
        (first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2"):
    second_player_won = True
    print("Second player won")
    exit()

# columns:

if (first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1") or \
        (first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1"):
    first_player_won = True
    print("First player won")
    exit()

elif (first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2") or \
        (first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2"):
    second_player_won = True
    print("Second player won")
    exit()


# rows:

for i in first_line:
    if i == "1":
        counter1_1 += 1
        if counter1_1 == 3:
            first_player_won = True
            print("First player won")
            exit()
    elif i == "2":
        counter2_1 += 1
        if counter2_1 == 3:
            second_player_won = True
            print("Second player won")
            exit()

for j in second_line:
    if j == "1":
        counter1_2 += 1
        if counter1_2 == 3:
            first_player_won = True
            print("First player won")
            exit()
    elif j == "2":
        counter2_2 += 1
        if counter2_2 == 3:
            second_player_won = True
            print("Second player won")
            exit()

for k in third_line:
    if k == "1":
        counter1_3 += 1
        if counter1_3 == 3:
            first_player_won = True
            print("First player won")
            exit()
    elif k == "2":
        counter2_3 += 1
        if counter2_3 == 3:
            second_player_won = True
            print("Second player won")
            exit()

if not first_player_won or not second_player_won:
    print("Draw!")
    exit()