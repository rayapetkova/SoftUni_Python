def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


# Test input:
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))






# 2 - this is not a solution for the task, but it's another way to do it (with kwargs)
#
# def get_info(**kwargs):
#     return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
# print(get_info(name="George", town="Sofia", age=20))
