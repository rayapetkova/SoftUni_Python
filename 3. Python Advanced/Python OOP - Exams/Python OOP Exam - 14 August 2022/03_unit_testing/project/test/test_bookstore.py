from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_initialization(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_total_sold_books_property(self):
        result = self.bookstore.total_sold_books

        self.assertEqual(0, result)

    def test_books_limit_raise_error_value_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        result = len(self.bookstore)

        self.assertEqual(60, result)

    def test_receive_book_raise_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 870, 'third': 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('random', 20)

        self.assertEqual(f"Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_book_title_not_in_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        result = self.bookstore.receive_book("random", 20)

        self.assertEqual({'first': 20, 'second': 30, 'third': 10, 'random': 20}, self.bookstore.availability_in_store_by_book_titles)

        self.assertEqual(f"20 copies of random are available in the bookstore.", result)

    def test_receive_book_book_title_in_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        result = self.bookstore.receive_book("first", 20)

        self.assertEqual({'first': 40, 'second': 30, 'third': 10}, self.bookstore.availability_in_store_by_book_titles)

        self.assertEqual(f"40 copies of first are available in the bookstore.", result)

    def test_sell_book_raise_exception_book_title_not_in_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('random', 20)

        self.assertEqual(f"Book random doesn't exist!", str(ex.exception))

    def test_sell_book_raise_exception_number_books_greater_than_available(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('first', 30)

        self.assertEqual(f"first has not enough copies to sell. Left: 20", str(ex.exception))

    def test_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        result = self.bookstore.sell_book('first', 10)

        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles['first'])
        self.assertEqual(10, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(f"Sold 10 copies of first", result)

    def test_sell_book_successfully2(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 20, 'second': 30, 'third': 10}

        result = self.bookstore.sell_book('first', 20)

        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles['first'])
        self.assertEqual(20, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual(f"Sold 20 copies of first", result)

    def test_str_method(self):
        self.bookstore.availability_in_store_by_book_titles = {'first': 10, 'second': 30, 'third': 10}
        self.bookstore._Bookstore__total_sold_books = 10

        result = str(self.bookstore)

        self.assertEqual(f"Total sold books: 10\nCurrent availability: 50\n"
                         f" - first: 10 copies\n - second: 30 copies\n - third: 10 copies", result)


if __name__ == '__main__':
    main()
