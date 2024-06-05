import datetime
import unittest

from classes import ClassicalConcert, JazzConcert, RockConcert
from manager import ConcertManager

class TestConcertManager(unittest.TestCase):
    def setUp(self):
        self.manager = ConcertManager()
        self.concert1 = RockConcert("Rock Night", datetime.date(2024, 6, 5), 50.0, ["Band A"], "Stadium")
        self.concert2 = JazzConcert("Jazz Evening", datetime.date(2024, 6, 6), 40.0, ["Band B"], "Club")
        self.concert3 = ClassicalConcert("Classical Morning", datetime.date(2024, 6, 7), 60.0, ["Band C"], "Hall")
        self.concert4 = RockConcert("Rock Fest", datetime.date(2024, 6, 10), 70.0, ["Band D"], "Arena")
        self.concert5 = JazzConcert("Jazz Festival", datetime.date(2024, 6, 11), 60.0, ["Band E"], "Park")
        self.concert6 = ClassicalConcert("Classical Night", datetime.date(2024, 6, 12), 80.0, ["Band F"], "Opera House")
        self.manager.create_concert(self.concert1)
        self.manager.create_concert(self.concert2)
        self.manager.create_concert(self.concert3)
        self.manager.create_concert(self.concert4)
        self.manager.create_concert(self.concert5)
        self.manager.create_concert(self.concert6)

    def test_create_concert(self):
        self.assertEqual(len(self.manager.concerts), 6)

    def test_read_concert(self):
        concert = self.manager.read_concert("Rock Night")
        self.assertEqual(concert.name, "Rock Night")

    def test_update_concert(self):
        self.manager.update_concert("Rock Night", {"price": 55.0})
        concert = self.manager.read_concert("Rock Night")
        self.assertEqual(concert.price, 55.0)

    def test_delete_concert(self):
        self.manager.delete_concert("Rock Night")
        self.assertEqual(len(self.manager.concerts), 5)

    def test_search_concerts(self):
        results = self.manager.search_concerts(genre="Jazz")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].name, "Jazz Evening")
        self.assertEqual(results[1].name, "Jazz Festival")

    def test_sort_concerts(self):
        sorted_concerts = self.manager.sort_concerts("price")
        self.assertEqual(sorted_concerts[0].name, "Jazz Evening")
        self.assertEqual(sorted_concerts[-1].name, "Classical Night")

    def test_book_seat(self):
        self.concert1.book_seat(1, "User1")
        self.assertEqual(self.concert1.bookings[1], "User1")

    def test_cancel_booking(self):
        self.concert1.book_seat(1, "User1")
        self.concert1.cancel_booking(1)
        self.assertNotIn(1, self.concert1.bookings)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
