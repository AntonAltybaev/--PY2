from typing import List


class Book:
    """
    Class represents Book entity
    """

    def __init__(self, id, name, pages):
        self.pages = pages
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f"Книга {self.name}"

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name={self.name}, pages={self.pages})"


class Library:
    """
    Class represents Library entity
    """

    def __init__(self, books: List[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
        :return: int
        """
        return len(self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id несуществует"
        :return: int
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id несуществует")
