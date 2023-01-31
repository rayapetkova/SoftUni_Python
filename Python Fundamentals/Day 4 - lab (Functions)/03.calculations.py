def calculation(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


current_operator = input()
current_a = int(input())
current_b = int(input())

print(calculation(current_operator, current_a, current_b))