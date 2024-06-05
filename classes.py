from typing import List, Dict, Any
import datetime

class ConcertEvent:
    def __init__(self, name: str, date: datetime.date, price: float, genre: str, performers: List[str], location: str):
        self.name = name
        self.date = date
        self.price = price
        self.genre = genre
        self.performers = performers
        self.location = location
        self.bookings = {}  # Ключ - номер місця, значення - ім'я користувача

    def book_seat(self, seat_number: int, user_name: str):
        if seat_number in self.bookings:
            raise ValueError("Місце вже заброньовано")
        self.bookings[seat_number] = user_name

    def cancel_booking(self, seat_number: int):
        if seat_number not in self.bookings:
            raise ValueError("Місце не було заброньовано")
        del self.bookings[seat_number]

class RockConcert(ConcertEvent):
    def __init__(self, name: str, date: datetime.date, price: float, performers: List[str], location: str):
        super().__init__(name, date, price, "Rock", performers, location)
        self._volume = 10  # Випадковим чином поставив

    def set_volume(self, volume: int):
        self._volume = volume

class JazzConcert(ConcertEvent):
    def __init__(self, name: str, date: datetime.date, price: float, performers: List[str], location: str):
        super().__init__(name, date, price, "Jazz", performers, location)
        self._instruments = ['Барабани', 'Сопілка']

    def set_instruments(self, instruments: List[str]):
        self._instruments = instruments

class ClassicalConcert(ConcertEvent):
    def __init__(self, name: str, date: datetime.date, price: float, performers: List[str], location: str):
        super().__init__(name, date, price, "Classical", performers, location)
        self._orchestra_size = 50  # Значення за замовчуванням

    def set_orchestra_size(self, orchestra_size: int):
        self._orchestra_size = orchestra_size