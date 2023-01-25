money = float(input())

coins = money * 100
coin_count = 0

while True:
    if coins >= 200:
        coins = coins - 200
        coin_count = coin_count + 1
    elif coins >= 100:
        coins = coins - 100
        coin_count = coin_count + 1
    elif coins >= 50:
        coins = coins - 50
        coin_count = coin_count + 1
    elif coins >= 20:
        coins = coins - 20
        coin_count = coin_count + 1
    elif coins >= 10:
        coins = coins - 10
        coin_count = coin_count + 1
    elif coins >= 5:
        coins = coins - 5
        coin_count = coin_count + 1
    elif coins >= 2:
        coins = coins - 2
        coin_count = coin_count + 1
    elif coins >= 1:
        coins = coins - 1
        coin_count = coin_count + 1
    else:
        break

print(coin_count)