from math import floor

balls_num = int(input())

num_red = 0
num_orange = 0
num_yellow = 0
num_white = 0
num_black = 0
num_others = 0
total = 0

for i in range(0, balls_num):
    colour = input()
    if colour == "red":
        num_red = num_red + 1
        total = total + 5
    elif colour == "orange":
        num_orange = num_orange + 1
        total = total + 10
    elif colour == "yellow":
        num_yellow = num_yellow + 1
        total = total + 15
    elif colour == "white":
        num_white = num_white + 1
        total = total + 20
    elif colour == "black":
        num_black = num_black + 1
        total = floor(total / 2)
    else:
        num_others = num_others + 1

print(f"Total points: {total}")
print(f"Red balls: {num_red}")
print(f"Orange balls: {num_orange}")
print(f"Yellow balls: {num_yellow}")
print(f"White balls: {num_white}")
print(f"Other colors picked: {num_others}")
print(f"Divides from black balls: {num_black}")