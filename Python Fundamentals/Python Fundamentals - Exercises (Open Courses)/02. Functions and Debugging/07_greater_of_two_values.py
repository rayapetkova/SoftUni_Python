def type_int(first, second):
    return second if int(second) > int(first) else first


def type_char(first, second):
    return second if ord(second) > ord(first) else first


def type_string(first, second):
    return second if second > first else first


type_given, first_input, second_input = input(), input(), input()
if type_given == "int":
    print(type_int(first_input, second_input))
elif type_given == "char":
    print(type_char(first_input, second_input))
else:
    print(type_string(first_input, second_input))
