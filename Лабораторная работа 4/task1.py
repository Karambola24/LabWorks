class Animal:
    """
    Базовый класс, представляющий животное
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Инициализация базового класса Animal
        :param name: Имя животного
        :param age: Возраст животного
        :param species: Вид животного
        """
        self._name = name  # инкапсуляция для защиты от изменения
        self._age = age
        self.species = species

    def __str__(self) -> str:
        return f"{self.species} по имени {self._name}, возраст: {self._age}"

    def __repr__(self) -> str:
        return f"Animal(name='{self._name}', age={self._age}, species='{self.species}')"

    def make_sound(self) -> str:
        """
        Метод с помощью которого животное издает звук (перегружен в дочерних классах)
        """
        return "Животное издает звук."

    def get_age(self) -> int:
        """
        Возвращает возраст животного.
        """
        return self._age


class Dog(Animal):
    """
    Дочерний класс собака
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация класса Dog с расширением конструктора
        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age, species="Собака")  # Унаследован конструктор Animal
        self.breed = breed  # Добавлен атрибут породы

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog
        """
        return f"{self.species} породы {self.breed} по имени {self._name}, возраст: {self._age}"

    def make_sound(self) -> str:
        """
        Перегруженный метод для издания звука собакой
        Причина перегрузки: собаки издают свой звук, не характерный для других животных
        """
        return "Гав-гав"

    def fetch(self, item: str) -> str:
        """
        Метод, уникальный для класса Dog, имитирующий действие "принести предмет"
        :param item: Название предмета
        :return: Строка с описанием действия
        """
        return f"{self._name} принес(ла) {item}."


class Cat(Animal):
    """
    Дочерний класс кошка
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация класса Cat с расширением конструктора
        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Цвет кошки (необязательный параметр)
        """
        super().__init__(name, age, species="Кошка")  # Унаследован конструктор Animal
        self._color = color  # Инкапсуляция цвета для ограничения прямого доступа

    def __str__(self) -> str:

        color_info = f" цвета {self._color}" if self._color else ""
        return f"{self.species}{color_info} по имени {self._name}, возраст: {self._age}"

    def make_sound(self) -> str:
        """
        Перегруженный метод для издания звука кошкой
        Причина перегрузки: кошки издают свой звук, не характерный для других животных
        """
        return "Мяу"

    def scratch(self) -> str:
        """
        Метод, уникальный для класса Cat, имитирующий действие "царапать"
        """
        return f"{self._name} царапается зараза!"


if __name__ == "__main__":
    dog = Dog(name="Барбос", age=2, breed="Лабрадор")
    print(dog)
    print(dog.make_sound())
    print(dog.fetch("палка"))

    cat = Cat(name="Нюша", age=8, color="серый")
    print(cat)
    print(cat.make_sound())
    print(cat.scratch())
    pass
