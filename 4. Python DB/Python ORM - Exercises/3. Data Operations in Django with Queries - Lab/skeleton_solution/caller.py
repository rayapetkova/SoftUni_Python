import os
import django
from datetime import datetime


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student


# Create and check models
def add_students():
    students = [('FC5204', 'John', 'Doe', '15/05/1995', 'john.doe@university.com'),
                ('FE0054', 'Jane', 'Smith', 'NULL', 'jane.smith@university.com'),
                ('FH2014', 'Alice', 'Johnson', '10/02/1998', 'alice.johnson@university.com'),
                ('FH2015', 'Bob', 'Wilson', '25/11/1996', 'bob.wilson@university.com')]

    for student in students:
        s_id, f_name, l_name, b_date, student_email = student

        if b_date == "NULL":
            curr_student = Student.objects.create(student_id=s_id,
                                                  first_name=f_name,
                                                  last_name=l_name,
                                                  email=student_email)
        else:
            curr_student = Student.objects.create(student_id=s_id,
                                                  first_name=f_name,
                                                  last_name=l_name,
                                                  birth_date=datetime.strptime("15/05/1995", "%d/%m/%Y").strftime("%Y-%m-%d"),
                                                  email=student_email)
        curr_student.save()


def get_students_info():
    students_records = Student.objects.all()

    all_students_info = []
    for student in students_records:
        all_students_info.append(f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}")

    return '\n'.join(all_students_info)


def update_students_emails():
    students_records = Student.objects.all()

    for student in students_records:
        student.email = student.email.replace("university.com", "uni-students.com")
        student.save()


def truncate_students():
    Student.objects.all().delete()


# Run and print your queries
# print(Student.objects.all())

# print(get_students_info())

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)

truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")
