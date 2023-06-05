import os

while True:
    line = input()

    if line == "End":
        break

    command = line.split("-")

    if "Create" in command:
        file_name = command[1]

        if os.path.isfile(f"txt_files/{file_name}"):

            with open(f"txt_files/{file_name}", "r+") as text_file:
                text_file.truncate(0)

        else:
            new_text_file = open(f"txt_files/{file_name}", "w")
            new_text_file.close()

    elif "Add" in command:
        file_name, content = command[1], command[2]

        with open(f"txt_files/{file_name}", "a") as text_file:
            text_file.write(f"{content}\n")

    elif "Replace" in command:
        file_name, old_string, new_string = command[1], command[2], command[3]

        if not os.path.isfile(f"txt_files/{file_name}"):
            print(f"An error occurred")
            continue

        with open(f"txt_files/{file_name}", "r+") as text_file:
            content = text_file.readlines()
            final = []

            for i in range(len(content)):
                content[i] = content[i].replace(f"{old_string}", f"{new_string}")
                final.append(content[i])

            text_file.seek(0)
            text_file.truncate(0)

            for l in final:
                text_file.write(l)

    elif "Delete" in command:
        file_name = command[1]

        if not os.path.isfile(f"txt_files/{file_name}"):
            print(f"An error occurred")
            continue

        os.remove(f"txt_files/{file_name}")
