import re

pattern = r"\d{2}[a-zA-z_]+"

copied_tasks = ""  # TODO: put your tasks here

copied_tasks = copied_tasks.replace(". ", "_")
copied_tasks = copied_tasks.replace(" ", "_")
copied_tasks = copied_tasks.replace("*", "")
copied_tasks = copied_tasks.lower()

matches = re.findall(pattern, copied_tasks)

for task in matches:
    print(task)
