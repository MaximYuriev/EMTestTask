from models.book import Book


class Library:
    books = []

    @classmethod
    def add_new_book(cls, book: Book):
        cls.books.append(book)

    @classmethod
    def get_all_books(cls) -> list:
        return cls.books

    @classmethod
    def get_book_by_id(cls, id_book: int) -> Book:
        for book in cls.books:
            if book.id == id_book:
                return book

    @classmethod
    def get_books_by_params(cls, **kwargs) -> list:
        founded_books = [book for book in cls.books]
        for book in cls.books:
            book_dict = book.__dict__
            for key, value in kwargs.items():
                if book_dict[key] != value:
                    founded_books.remove(book)
                    break
        return founded_books

    @classmethod
    def delete_book(cls, book: Book):
        cls.books.remove(book)