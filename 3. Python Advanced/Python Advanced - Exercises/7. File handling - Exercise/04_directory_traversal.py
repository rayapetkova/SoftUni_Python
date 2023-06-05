import os


def find_files(directory):
    for name in os.listdir(directory):

        current_file_path = os.path.join(directory, name)

        if os.path.isfile(current_file_path):
            extension = "." + current_file_path.split(".")[-1]
            dictionary_output[extension] = dictionary_output.get(extension, []) + [name]

        elif os.path.isdir(current_file_path):
            find_files(current_file_path)

    final = []

    for c_extension, all_files in dictionary_output.items():
        final.append(c_extension)

        for some_file in all_files:
            final.append(f"- - - {some_file}")

    return '\n'.join(final)


directory_given = input()
dictionary_output = {}

print(find_files(directory_given))
