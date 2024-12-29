# TODO: описать базовый класс
class Animal:
    """
    Базовый класс для всех животных.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def speak(self) -> str:
        """Возвращает звук, который издает животное. По умолчанию - 'издает звук'."""
        return "издает звук"

    def __str__(self) -> str:
        """Возвращает возраст животного."""
        return f"{self.name}, {self.age} лет"

    def __repr__(self) -> str:
        """Возвращает описание животного.."""
        return f"Animal(name='{self.name}', age={self.age})"

# TODO: описать дочерний класс
class Cat(Animal):
    """
    Класс для кошек, наследующий от Animal.

    Атрибуты:
        color (str): Цвет шерсти кошки.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__color = color  # Непубличный атрибут

    def speak(self) -> str:
        """Возвращает звук, который издает кошка."""
        return "мяу"

    def __str__(self) -> str:
        """Возвращает цвет шерсти."""
        return f"{super().__str__()} - Цвет: {self.__color}"

    def __repr__(self) -> str:
        """Возвращает описание кошки."""
        return f"Cat(name='{self.name}', age={self.age}, color='{self.__color}')"


class Dog(Animal):
    """
    Класс для собак, наследующий от Animal.

    Атрибуты:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__breed = breed  # Непубличный атрибут

    def speak(self) -> str:
        """Возвращает звук, который издает собака."""
        return "гав"

    def __str__(self) -> str:
        """Возвращает породу собаки"""
        return f"{super().__str__()} - Порода: {self.__breed}"

    def __repr__(self) -> str:
        """Возвращает описание собаки."""
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.__breed}')"


class Horse(Animal):
    """
    Класс для лошадей, наследующий от Animal.

    Атрибуты:
        breed (str): Порода лошади.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__breed = breed  # Непубличный атрибут

    def speak(self) -> str:
        """Возвращает звук, который издает лошадь."""
        return "игого"

    def saddle(self) -> str:
        """Метод для оседлания лошади.

        Возвращает сообщение о том, что лошадь оседлана.
        """
        return f"{self.name} оседлана и готова к поездке!"

    def __str__(self) -> str:
        """Возвращает породу лошади."""
        return f"{super().__str__()} - Порода: {self.__breed}"

    def __repr__(self) -> str:
        """Возвращает описание лошади."""
        return f"Horse(name='{self.name}', age={self.age}, breed='{self.__breed}')"


class Chicken(Animal):
    """
    Класс для куриц, наследующий от Animal.

    Атрибуты:
        egg_color (str): Цвет яиц, которые несет курица.
    """

    def __init__(self, name: str, age: int, egg_color: str) -> None:
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__egg_color = egg_color  # Непубличный атрибут

    def speak(self) -> str:
        """Возвращает звук, который издает курица."""
        return "ко-ко"

    def __str__(self) -> str:
        """Возвращает цвет яиц, которые несет курица."""
        return f"{super().__str__()} - Цвет яиц: {self.__egg_color}"

    def __repr__(self) -> str:
        """Возвращает описание курицы."""
        return f"Chicken(name='{self.name}', age={self.age}, egg_color='{self.__egg_color}')"

# Пример использования классов

if __name__ == "__main__":
    cat = Cat("Мурка", 3, "Черный")
    print(cat)  # Мурка, 3 лет - Цвет: Черный
    print(cat.speak())  # мяу
    print(repr(cat))  # Cat(name='Мурка', age=3, color='Черный')

    dog = Dog("Бобик", 5, "Лабрадор")
    print(dog)  # Бобик, 5 лет - Порода: Лабрадор
    print(dog.speak())  # гав
    print(repr(dog))  # Dog(name='Бобик', age=5, breed='Лабрадор')

    horse = Horse("Скакун", 7, "Арабская")
    print(horse)  # Скакун, 7 лет - Порода: Арабская
    print(horse.speak())  # игого
    print(horse.saddle())  # Скакун оседлана и готова к поездке!
    print(repr(horse))  # Horse(name='Скакун', age=7, breed='Арабская')

    chicken = Chicken("Несушка", 2, "Белый")
    print(chicken)  # Несушка, 2 лет - Цвет яиц: Белый
    print(chicken.speak())  # ко-ко
    print(repr(chicken))  # Chicken(name='Несушка', age=2, egg_color='Белый')
