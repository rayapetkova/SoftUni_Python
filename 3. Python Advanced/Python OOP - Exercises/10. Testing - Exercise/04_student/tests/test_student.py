from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("TestName")

    def test_initialization(self):
        self.assertEqual("TestName", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_method_course_name_already_in_courses_dictionary(self):
        self.student.courses["Python"] = ["somenote"]

        result = self.student.enroll("Python", ["note1", "note2"])

        self.assertEqual(["somenote", "note1", "note2"], self.student.courses["Python"])
        self.assertEqual(f"Course already added. Notes have been updated.", result)

    def test_enroll_method_check_if_add_course_notes_is_empty_string(self):
        result = self.student.enroll("Python", ["note1", "note2"])

        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)
        self.assertEqual(f"Course and course notes have been added.", result)

    def test_enroll_method_check_if_add_course_notes_is_y(self):
        result = self.student.enroll("Python", ["note1", "note2"], "Y")

        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)
        self.assertEqual(f"Course and course notes have been added.", result)

    def test_enroll_method_if_course_name_not_in_courses_and_add_course_notes_not_y_or_empty_string(self):
        result = self.student.enroll("Python", ["note1", "note2"], "random")

        self.assertEqual({"Python": []}, self.student.courses)
        self.assertEqual(f"Course has been added.", result)

    def test_add_notes_method_when_course_name_in_courses(self):
        self.student.courses["Python"] = ["note1", "note2"]

        result = self.student.add_notes("Python", ["note3", "note4"])

        self.assertEqual({"Python": ["note1", "note2", ["note3", "note4"]]}, self.student.courses)
        self.assertEqual(f"Notes have been updated", result)

    def test_add_notes_method_raise_exception_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", ["firstnote", "secondnote"])

        self.assertEqual(f"Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_method_if_course_name_in_courses(self):
        self.student.courses["Python"] = ["note1", "note2"]

        result = self.student.leave_course("Python")

        self.assertEqual({}, self.student.courses)
        self.assertEqual(f"Course has been removed", result)

    def test_leave_course_method_raise_exception_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")

        self.assertEqual(f"Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
