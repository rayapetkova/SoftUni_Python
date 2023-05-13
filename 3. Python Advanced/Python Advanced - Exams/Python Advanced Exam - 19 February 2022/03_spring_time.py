def start_spring(**kwargs):
    dictionary, final = {}, []
    for key, value in kwargs.items():
        dictionary[value] = dictionary.get(value, []) + [key]

    sorted_dict = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
    for c_type, spring_objects in sorted_dict:
        sorted_spring_objects = sorted(spring_objects)

        final.append(f"{c_type}:")
        for some_object in sorted_spring_objects:
            final.append(f"-{some_object}")

    return '\n'.join(final)


# Test input:

# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))


# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))


# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
