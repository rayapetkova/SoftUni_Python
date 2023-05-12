def flights(*args):
    dictionary = {}
    idx = 0
    while True:
        if args[idx] == "Finish" or args[idx + 1] == "Finish":
            break
        dictionary[args[idx]] = dictionary.get(args[idx], 0) + args[idx + 1]
        idx += 2
    return dictionary


# Test inputs:

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
#
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
