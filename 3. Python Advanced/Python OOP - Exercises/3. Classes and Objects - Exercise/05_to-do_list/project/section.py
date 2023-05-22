from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.cleaned = 0

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        for task in self.tasks:
            if task.completed:
                self.cleaned += 1
                self.tasks.remove(task)

        return f"Cleared {self.cleaned} tasks."

    def view_section(self):
        final = []

        final.append(f"Section {self.name}:")

        for task in self.tasks:
            final.append(f"{task.details()}")

        return '\n'.join(final)


# Test code:

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
