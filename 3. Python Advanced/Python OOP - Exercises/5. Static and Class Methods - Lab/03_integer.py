from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))

        return f"value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        final = 0

        for i in range(len(value)):
            if i + 1 == len(value) or roman_nums[value[i]] >= roman_nums[value[i + 1]]:
                final += roman_nums[value[i]]
            else:
                final -= roman_nums[value[i]]

        return cls(final)


    @classmethod
    def from_string(cls, value):
        if str(value).isdigit():
            return cls(int(value))

        return f"wrong type"


# Test code:

# first_num = Integer(10)
# print(first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num.value)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
