tasks = []  # Put your tasks here

for task in tasks:
    task = task.replace(". ", "_")
    task = task.replace(" ", "_")
    task = task.replace("*", "")
    task = task.lower()
    print(task)
