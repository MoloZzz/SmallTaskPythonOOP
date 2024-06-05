from typing import Any, Dict, List
from classes import ConcertEvent


class ConcertManager:
    def __init__(self):
        self.concerts = []

    def create_concert(self, concert: ConcertEvent):
        self.concerts.append(concert)

    def read_concert(self, name: str) -> ConcertEvent:
        for concert in self.concerts:
            if concert.name == name:
                return concert
        raise ValueError("Концерт не знайдено")

    def update_concert(self, name: str, updated_info: Dict[str, Any]):
        concert = self.read_concert(name)
        for key, value in updated_info.items():
            if hasattr(concert, key):
                setattr(concert, key, value)
            else:
                raise ValueError(f"Неправильний параметр: {key}")

    def delete_concert(self, name: str):
        concert = self.read_concert(name)
        self.concerts.remove(concert)

    def search_concerts(self, **kwargs) -> List[ConcertEvent]:
        results = self.concerts
        for key, value in kwargs.items():
            results = [concert for concert in results if getattr(concert, key) == value]
        return results

    def sort_concerts(self, key: str) -> List[ConcertEvent]:
        return sorted(self.concerts, key=lambda concert: getattr(concert, key))
