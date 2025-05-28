from abc import ABC

from app.book import Book


class Display(ABC):
    def display(self, book: Book) -> None:
        self.book = book
        pass


class DisplayRight(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayRevers(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
