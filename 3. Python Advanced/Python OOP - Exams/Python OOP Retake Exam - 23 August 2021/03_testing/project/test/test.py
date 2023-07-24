from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Random')

    def test_initialization(self):
        self.assertEqual('Random', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_raise_error_name_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual(f"Name cannot be empty string!", str(ve.exception))

    def test_add_book_method(self):
        self.library.books_by_authors = {'first': ['ok', 'ok1'], 'second': ['idk', 'idk1']}

        self.library.add_book('third', 'some_title')

        self.assertEqual({'first': ['ok', 'ok1'], 'second': ['idk', 'idk1'], 'third': ['some_title']}, self.library.books_by_authors)

    def test_add_book_method1(self):
        self.library.books_by_authors = {'first': ['ok', 'ok1'], 'second': ['idk', 'idk1']}

        self.library.add_book('first', 'some_title')

        self.assertEqual({'first': ['ok', 'ok1', 'some_title'], 'second': ['idk', 'idk1']}, self.library.books_by_authors)

    def test_add_reader_name_not_in_readers(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}

        self.library.add_reader('reader3')

        self.assertEqual({'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2'], 'reader3': []}, self.library.readers)

    def test_add_reader_reader_in_readers(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}

        result = self.library.add_reader('reader1')

        self.assertEqual(f"reader1 is already registered in the Random library.", result)

    def test_rent_book_reader_name_not_in_readers(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}

        result = self.library.rent_book('reader3333', 'book_author', 'book_title')

        self.assertEqual(f"reader3333 is not registered in the Random Library.", result)

    def test_rent_book_book_author_not_in_books_by_authors(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}
        self.library.books_by_authors = {'first': ['ok', 'ok1'], 'second': ['idk', 'idk1']}

        result = self.library.rent_book('reader1', 'third', 'book_title')

        self.assertEqual(f"Random Library does not have any third's books.", result)

    def test_rent_book_book_title_not_in_book_by_authors_book_author(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}
        self.library.books_by_authors = {'first': ['ok', 'ok1'], 'second': ['idk', 'idk1']}

        result = self.library.rent_book('reader1', 'first', 'not_valid')

        self.assertEqual(f"""Random Library does not have first's "not_valid".""", result)

    def test_rent_book_successfully(self):
        self.library.readers = {'reader1': ['okay1', 'idkkk'], 'reader2': ['okay2']}
        self.library.books_by_authors = {'first': ['ok', 'ok1'], 'second': ['idk', 'idk1']}

        self.library.rent_book('reader1', 'first', 'ok')

        self.assertEqual({'reader1': ['okay1', 'idkkk', {'first': 'ok'}], 'reader2': ['okay2']}, self.library.readers)
        self.assertEqual({'first': ['ok1'], 'second': ['idk', 'idk1']}, self.library.books_by_authors)


if __name__ == "__main__":
    main()
