class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Возвращает название книги. """
        return self._name

    @property
    def author(self) -> str:
        """ Возвращает автора книги. """
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц. """
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги. """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"



if __name__ == '__main__':
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Война и мир", "Лев Толстой", 60.5)

    print(paper_book)
    print(repr(paper_book))

    print(audio_book)
    print(repr(audio_book))
