from enum import Enum


class BookStatus(Enum):
    IN_STOCK = "В наличии"
    GIVEN_OUT = "Выдана"


class Book:
    id = 0

    def __init__(self, title: str, author: str, year: str):
        self.increment_id()
        self.id = Book.id
        self.title = title
        self.author = author
        self.year = year
        self.status = BookStatus.IN_STOCK.value

    def __repr__(self):
        return f'id: {self.id} title: {self.title} author: {self.author} year: {self.year} status: {self.status}'

    def update_status(self, status: BookStatus):
        self.status = status.value

    @classmethod
    def increment_id(cls):
        cls.id += 1
