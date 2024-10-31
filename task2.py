from abc import ABC, abstractmethod

from logger import logger


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} ({self.year}) by {self.author}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        for book in self.books:
            logger.info(book)


class LibraryManager:
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
