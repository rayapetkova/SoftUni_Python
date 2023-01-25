width = int(input())
length = int(input())

cake_pieces = width * length
eaten_pieces = 0

while True:
    pieces = input()
    if pieces != "STOP":
        pieces = int(pieces)
        eaten_pieces = eaten_pieces + pieces
        if eaten_pieces >= cake_pieces:
            print(f"No more cake left! You need {eaten_pieces - cake_pieces} pieces more.")
            break

    if pieces == "STOP":
        if eaten_pieces >= cake_pieces:
            print(f"No more cake left! You need {eaten_pieces - cake_pieces} pieces more.")
        else:
            print(f"{cake_pieces - eaten_pieces} pieces are left.")
        break