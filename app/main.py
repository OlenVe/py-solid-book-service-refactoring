import json
import xml.etree.ElementTree as elementTree
from abc import ABC


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class Display(ABC):
    @staticmethod
    def display(self, book: Book) -> None:
        self.book = book
        pass


class DisplayRight(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayRevers(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Print(ABC):
    @staticmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintRight(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Serializer(ABC):
    @staticmethod
    def serialize(self, book: Book) -> None:
        pass


class SerializerJson(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(Serializer):
    def serialize(self, book: Book) -> str:
        root = elementTree.Element("book")
        title = elementTree.SubElement(root, "title")
        title.text = book.title
        content = elementTree.SubElement(root, "content")
        content.text = book.content
        return elementTree.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display = {
        "console": DisplayRight(),
        "reverse": DisplayRevers(),
    }
    print_b = {
        "console": PrintRight(),
        "reverse": PrintReverse(),
    }
    serializer = {
        "json": SerializerJson(),
        "xml": SerializerXML(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display.get(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = print_b.get(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = serializer.get(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
