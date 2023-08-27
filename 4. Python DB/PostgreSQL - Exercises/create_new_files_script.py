import os
import re

"""MAKE NEW DIRECTORY"""
new_directory_name = input("Enter new directory name: ")
if not os.path.exists(new_directory_name):
    os.makedirs(new_directory_name)

"""REPLACE CHARACTERS"""
all_tasks = ''.join(symbol for symbol in input("Enter tasks: ") if symbol.isalnum() or symbol.isspace() or symbol == "*")
all_tasks = all_tasks.replace(".", "")
all_tasks = all_tasks.replace(" *", "")
all_tasks = all_tasks.replace(" ", "_")
all_tasks = all_tasks.lower()

"""ENTER FILE TYPE"""
file_type = input("Enter file type (.py/.sql/.html/.css etc.): ")

"""REGEX MATCHES"""
regex_pattern = r"\d{1,2}[^\d]+"
matches = re.findall(regex_pattern, all_tasks)

for task_name in matches:
    new_file = os.path.join(new_directory_name, task_name + file_type)

    with open(new_file, "w") as task:
        pass
