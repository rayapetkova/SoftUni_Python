def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


number = int(input())
print(f"The number {number} is {check_number(number)}.")