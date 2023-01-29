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