def words_sorting(*args):
    dictionary, final_output = {}, []
    for word in args:
        dictionary[word] = sum(ord(symbol) for symbol in word)

    sorted_dict = dictionary
    if sum(dictionary.values()) % 2 != 0:
        sorted_dict = sorted(dictionary.items(), key=lambda x: -x[1])
    else:
        sorted_dict = sorted(dictionary.items(), key=lambda x: x[0])

    for key, value in sorted_dict:
        final_output.append(f"{key} - {value}")

    return '\n'.join(final_output)


# Test input:

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))
