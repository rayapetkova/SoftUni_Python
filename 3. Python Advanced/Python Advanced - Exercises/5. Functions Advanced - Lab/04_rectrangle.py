def rectangle(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return f"Enter valid values!"

    def area(curr_a, curr_b):
        return curr_a * curr_b

    def perimeter(curr_a, curr_b):
        return 2*curr_a + 2*curr_b

    return f"Rectangle area: {area(a, b)}\nRectangle perimeter: {perimeter(a, b)}"


# Test inputs:
# print(rectangle(2, 10))
# print(rectangle('2', 10))
