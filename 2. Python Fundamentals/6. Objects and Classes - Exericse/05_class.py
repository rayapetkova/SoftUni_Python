class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name, student_grade):
        if Class.__students_count > 0:
            self.students.append(student_name)
            self.grades.append(student_grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return average

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {(self.get_average_grade()):.2f}"
