# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param brand: Марка транспортного средства
        :param model: Модель транспортного средства
        :param year: Год выпуска

        Примеры:
        >>> vehicle = Vehicle("Skoda", "Octavia", 2005)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year < 1895:  # Год основания Skoda
            raise ValueError("Год выпуска должен быть целым числом и не меньше 1895")

        self.make = brand
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Skoda", "Octavia", 2005)
        >>> vehicle.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.

        Примеры:
        >>> vehicle = Vehicle("Skoda", "Octavia", 2005)
        >>> vehicle.stop_engine()
        """
        ...


class UnitedKingdom:
    def __init__(self, population: int, area: float, monarch: str):
        """
        Создание и подготовка к работе объекта "Великобритания".

        :param population: Население страны.
        :param area: Площадь страны (в квадратных километрах).
        :param monarch: Имя текущего монарха.

        Примеры:
        >>> uk = UnitedKingdom(67000000, 243610.0, "Чарльз III")
        """
        if not isinstance(population, int) or population <= 0:
            raise ValueError("Население должно быть положительным целым числом")
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        if not isinstance(monarch, str) or not monarch:
            raise ValueError("Имя монарха должно быть непустой строкой")

        self.population = population
        self.area = area
        self.monarch = monarch

    def calculate_population_density(self) -> float:
        """
        Вычисление плотности населения (человек на квадратный километр).

        :return: Плотность населения.

        Примеры:
        >>> uk = UnitedKingdom(67000000, 243610.0, "Чарльз III")
        >>> round(uk.calculate_population_density(), 2)
        275.03
        """
        return self.population / self.area

    def change_monarch(self, new_monarch: str) -> None:
        """
        Смена монарха.

        :param new_monarch: Имя нового монарха.
        :raise ValueError: Если имя нового монарха не является строкой или пустое.

        Примеры:
        >>> uk = UnitedKingdom(67_000_000, 243_610.0, "Чарльз III")
        >>> uk.change_monarch("Вильям V")
        """
        if not isinstance(new_monarch, str) or not new_monarch:
            raise ValueError("Имя нового монарха должно быть непустой строкой")
        self.monarch = new_monarch

    def join_union(self, union_name: str) -> str:
        """
        Присоединение к международному союзу.

        :param union_name: Название союза.
        :return: Сообщение о присоединении.

        Примеры:
        >>> uk = UnitedKingdom(67_000_000, 243_610.0, "Чарльз III")
        >>> uk.join_union("ЕС")
        'Великобритания присоединилась к союзу ЕС.'
        """
        if not isinstance(union_name, str) or not union_name:
            raise ValueError("Название союза должно быть непустой строкой")
        return f"Великобритания присоединилась к союзу {union_name}."


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево".

        :param species: Вид дерева (например, "дуб", "сосна").
        :param age: Возраст дерева в годах.
        :param height: Высота дерева в метрах.

        Примеры:
        >>> oak = Tree("дуб", 50, 20.5)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличение возраста и высоты дерева.

        :param years: Количество лет, на которое дерево "стареет".
        :raise ValueError: Если количество лет отрицательное.

        Примеры:
        >>> oak = Tree("дуб", 50, 20.5)
        >>> oak.grow(5)
        """
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом")
        ...

    def shed_leaves(self, season: str) -> None:
        """
        Сбрасывание листьев в определенный сезон.

        :param season: Сезон года (например, "осень").
        :raise ValueError: Если сезон не является строкой или не поддерживается.

        Примеры:
        >>> oak = Tree("дуб", 50, 20.5)
        >>> oak.shed_leaves("осень")
        """
        if season not in ["осень", "зима"]:
            raise ValueError("Сезон должен быть 'осень' или 'зима'")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
