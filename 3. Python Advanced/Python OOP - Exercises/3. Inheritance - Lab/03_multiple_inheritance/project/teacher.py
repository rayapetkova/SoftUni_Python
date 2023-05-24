from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return f"teaching..."


# Test code:

# t = Teacher()
# print(t.get_fired())
# print(t.sleep())
# print(t.teach())
