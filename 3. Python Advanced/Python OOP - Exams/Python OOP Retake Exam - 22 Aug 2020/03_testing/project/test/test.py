from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.report_card = StudentReportCard("Random", 10)

    def test_initialization(self):
        self.assertEqual("Random", self.report_card.student_name)
        self.assertEqual(10, self.report_card.school_year)
        self.assertEqual({}, self.report_card.grades_by_subject)

    def test_successful_year(self):
        self.report_card.school_year = 1

        self.assertEqual(1, self.report_card.school_year)

    def test_successful_year_1(self):
        self.report_card.school_year = 12

        self.assertEqual(12, self.report_card.school_year)

    def test_student_name_raise_error_value_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.report_card.student_name = ""

        self.assertEqual(f"Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_raise_value_error_value_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.report_card.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_raise_value_error_value_greater_than_twelve(self):
        with self.assertRaises(ValueError) as ve:
            self.report_card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_method_subject_not_in_grades_by_subject_dictionary(self):
        self.report_card.grades_by_subject = {'first': [2, 3, 4], 'second': [6, 5, 4]}

        self.report_card.add_grade('third', 6)

        self.assertEqual({'first': [2, 3, 4], 'second': [6, 5, 4], 'third': [6]}, self.report_card.grades_by_subject)

    def test_add_grade_method_subject_in_grades_by_subject_dictionary(self):
        self.report_card.grades_by_subject = {'first': [2, 3, 4], 'second': [6, 5, 4]}

        self.report_card.add_grade('first', 5)

        self.assertEqual({'first': [2, 3, 4, 5], 'second': [6, 5, 4]}, self.report_card.grades_by_subject)

    def test_average_grade_by_subject_method(self):
        self.report_card.grades_by_subject = {'first': [2, 3, 4], 'second': [6, 5, 4]}

        result = self.report_card.average_grade_by_subject()

        self.assertEqual(f"first: 3.00\nsecond: 5.00", result)

    def test_average_grade_for_all_subjects_method(self):
        self.report_card.grades_by_subject = {'first': [2, 3, 4], 'second': [6, 5, 4]}

        result = self.report_card.average_grade_for_all_subjects()

        self.assertEqual(f"Average Grade: 4.00", result)

    def test_repr_method(self):
        self.report_card.grades_by_subject = {'first': [2, 3, 4], 'second': [6, 5, 4]}

        result = str(self.report_card)

        self.assertEqual(f"Name: Random\n"
                         f"Year: 10\n"
                         f"----------\n"
                         f"first: 3.00\nsecond: 5.00\n"
                         f"----------\n"
                         f"Average Grade: 4.00", result)


if __name__ == "__main__":
    main()