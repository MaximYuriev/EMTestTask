import time

from models.book import Book, BookStatus
from models.library import Library


class ConsoleInterface:
    run = True

    @staticmethod
    def start():
        print("-" * 100)
        time.sleep(1)
        print("Что Вы хотите сделать?\n"
              "1. Добавить книгу\n"
              "2. Удалить книгу\n"
              "3. Найти книгу\n"
              "4. Вывести список всех книг\n"
              "5. Изменить статус книги\n"
              "6. Завершить работу программы")
        choice = input("Ваше действие: ")
        print("-" * 100)
        if choice == '1':
            ConsoleInterface.add_book()
        elif choice == '2':
            ConsoleInterface.delete_book()
        elif choice == '3':
            ConsoleInterface.find_book()
        elif choice == '4':
            ConsoleInterface.print_all_books()
        elif choice == '5':
            ConsoleInterface.change_book_status()
        elif choice == '6':
            print("Завершаю работу программы!")
            ConsoleInterface.run = False
        else:
            print(f"Ошибка! Некорректный ввод! Вы ввели {choice}, а ожидалась цифра от 1 до 6!")

    @staticmethod
    def add_book():
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        book = Book(title=title, author=author, year=year)
        Library.add_new_book(book)
        print('Книга успешно добавлена!')

    @staticmethod
    def get_book_by_id() -> Book:
        try:
            input_id = input("Введите id книги: ")
            id_book = int(input_id)
            return Library.get_book_by_id(id_book)
        except ValueError:
            print(f'Ожидалось целочисленное значение! Вы ввели {input_id}')

    @staticmethod
    def print_all_books():
        books = Library.get_all_books()
        if not books:
            print("Книги не найдены!")
            return
        ConsoleInterface.print_books(books)

    @staticmethod
    def delete_book():
        book = ConsoleInterface.get_book_by_id()
        if book is None:
            print("Книга не найдена!")
            return
        Library.delete_book(book)
        print("Книга успешно удалена!")

    @staticmethod
    def find_book():
        print("Укажите параметры поиска:\n"
              "1. Название\n"
              "2. Автор\n"
              "3. Год издания")
        search_options = {}
        input_parameters = (
            input("Выбранные параметры (в случае множественного выбора используйте пробел в качестве разделителя): ")
        )
        if not input_parameters:
            print("Список параметров не может быть пустым!")
            return
        set_parameters = set(input_parameters.split(" "))
        for parameter in set_parameters:
            if parameter == '1':
                title = input("Введите название: ")
                search_options.update(title=title)
            elif parameter == '2':
                author = input("Введите имя автора: ")
                search_options.update(author=author)
            elif parameter == '3':
                year = input("Введите год издания: ")
                search_options.update(year=year)
            else:
                print(f"Ошибка! Некорректный ввод! Вы ввели {parameter}, а ожидалась цифра от 1 до 3!")
                return
        books = Library.get_books_by_params(**search_options)
        if books:
            return ConsoleInterface.print_books(books)
        print("Книги не найдены!")

    @staticmethod
    def change_book_status():
        book = ConsoleInterface.get_book_by_id()
        if book is None:
            print("Книга не найдена!")
            return
        print("Выберите статус, который хотите установить:\n"
              "1. В наличии\n"
              "2. Выдана")
        update_status_choice = input("Ваш выбор: ")
        if update_status_choice == '1':
            status = BookStatus.IN_STOCK
        elif update_status_choice == '2':
            status = BookStatus.GIVEN_OUT
        else:
            print(f"Ошибка! Некорректный ввод! Вы ввели {update_status_choice}, а ожидалась цифра от 1 до 2!")
            return
        book.update_status(status=status)
        print("Статус книги успешно изменен!")

    @staticmethod
    def print_books(books: list[Book]):
        for book in books:
            print(book)
