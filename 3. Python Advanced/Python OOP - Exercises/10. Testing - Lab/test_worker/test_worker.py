from unittest import TestCase, main
from test_worker_code import Worker  # This line needs to be commented if submitting to judge


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("TestWorker", 2000, 40)

    def test_initialization(self):
        self.assertEqual("TestWorker", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(40, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_working_raise_exception_for_zero_or_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual(f"Not enough energy.", str(ex.exception))

    def test_working_add_money_decrease_energy(self):
        self.worker.work()
        self.assertEqual(2000, self.worker.money)
        self.assertEqual(39, self.worker.energy)

    def test_rest_increase_energy(self):
        self.worker.rest()
        self.assertEqual(41, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f"TestWorker has saved 0 money.", self.worker.get_info())


if __name__ == '__main__':
    main()