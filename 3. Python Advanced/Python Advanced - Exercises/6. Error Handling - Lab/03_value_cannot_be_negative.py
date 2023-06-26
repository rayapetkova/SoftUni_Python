class ValueCannotBeNegative(Exception):
    """Value cannot be negative"""


for i in range(5):
    number = int(input())
    
    if number < 0:
        raise ValueCannotBeNegative
