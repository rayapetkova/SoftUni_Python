def result(text, given_input):
    if text == "int":
        total = float(given_input) * 2
        return f"{total:.0f}"
    elif text == "real":
        total = float(given_input) * 1.5
        return f"{total:.2f}"
    elif text == "string":
        return f"${given_input}$"


current_text = input()
current_given_input = input()
print(result(current_text, current_given_input))