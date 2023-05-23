def concatenate(*args, **kwargs):
    result = "".join(args)

    for word in kwargs.keys():
        result = result.replace(word, kwargs[word])

    return result


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
