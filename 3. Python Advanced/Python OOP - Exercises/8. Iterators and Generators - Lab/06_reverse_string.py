def reverse_text(text):
    idx = -1

    while abs(idx) <= len(text):
        yield text[idx]
        idx -= 1


# Test code:
# for char in reverse_text("step"):
#     print(char, end='')
