# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Инициализация объекта "Бутылка"
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> bottle = Bottle(780, 0) #инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
             raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <=0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой

        :return: Является ли бутылка пустой

        Примеры:
         >>> bottle = Bottle(780, 0)
         >>> bottle.is_empty_botlle()
        """
        ...

    def add_water_to_botlle(self, water: float) -> None:
        """

        Добавление воды в бутылку.

        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>>bottle = Bottle(780, 0)
        >>>bottle.add_water_to_botlle(300)
       """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")
        ...

    def remove_water_from_bottle(self, estimate_water: float) -> None:
        """
        Извлечение воды из бутылки.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бутылке, то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>>bottle = Bottle(780, 780)
        >>>bottle.remove_water_from_bottle(300)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примера, который находится в документации


    class Table:
        def __init__(self, material: str, length: float, width: float):
            """
            Инициализация объекта стола.

            :param material: Материал, из которого изготовлен стол.
            :param length: Длина стола в см. Должна быть больше 0.
            :param width: Ширина стола в см. Должна быть больше 0.
            :raises ValueError: Если длина или ширина <= 0.
            """
            if length <= 0:
                raise ValueError("Длина стола должна быть больше 0.")
            if width <= 0:
                raise ValueError("Ширина стола должна быть больше 0.")

            self.material = material
            self.length = length  # В сантиметрах
            self.width = width  # В сантиметрах

        def resize(self, new_length: float, new_width: float) -> None:
            """
            Изменяет размеры стола.

            :param new_length: Новая длина стола в см. Должна быть больше 0.
            :param new_width: Новая ширина стола в см. Должна быть больше 0.
            :raises ValueError: Если новая длина или ширина <= 0.
            """
            if new_length <= 0:
                raise ValueError("Новая длина стола должна быть больше 0.")
            if new_width <= 0:
                raise ValueError("Новая ширина стола должна быть больше 0.")

            self.length = new_length
            self.width = new_width

        def describe(self) -> str:
            """
            Возвращает строку с описанием стола.

            :return: Информация о материале, длине и ширине стола.
            """
            return f"Стол из {self.material}, размер {self.length} см x {self.width} см."

        def clean(self) -> str:
            """
            Описывает действие по очистке стола.

            :return: Сообщение о том, что стол очищен.
            """
            return "Стол очищен."


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация объекта дерева.

        :param species: Вид дерева.
        :param height: Высота дерева в метрах. Должна быть больше 0.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.
        :raises ValueError: если высота <= 0 или возраст < 0.
        """
        if height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.species = species
        self.height = height  # В метрах
        self.age = age  # В годах

    def grow(self, additional_height: float) -> None:
        """
        Увеличивает высоту дерева.

        :param additional_height: Дополнительная высота в метрах, на которую вырастет дерево.
        :raises ValueError: если дополнительная высота <= 0.
        """
        if additional_height <= 0:
            raise ValueError("Дополнительная высота должна быть больше 0.")

        self.height += additional_height

    def age_tree(self, years: int) -> None:
        """
        Увеличивает возраст дерева.

        :param years: Количество лет, на которое увеличится возраст дерева.
        :raises ValueError: если количество лет < 0.
        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")

        self.age += years

    def describe(self) -> str:
        """
        Возвращает строку с описанием дерева.

        :return: Информация о виде, высоте и возрасте дерева.
        """
        return f"Дерево вида '{self.species}', высота {self.height} м, возраст {self.age} года."
