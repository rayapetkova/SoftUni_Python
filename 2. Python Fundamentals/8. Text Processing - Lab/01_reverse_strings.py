while True:
    line = input()
    if line == "end":
        break
    print(f"{line} = {line[::-1]}")