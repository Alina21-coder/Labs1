class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        """
        return f"{self.make} {self.model} engine started."

    def __str__(self) -> str:
        """Переопределение строкового представления класса."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Представление объекта для отладки."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Класс легковых автомобилей, наследующий от Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, num_doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param num_doors: Количество дверей в автомобиле.
        """
        super().__init__(make, model, year)
        self.__num_doors = num_doors  # Инкапсуляция атрибута, чтобы защитить его от изменения

    def get_num_doors(self) -> int:
        """
        Получить количество дверей.

        :return: Количество дверей легкового автомобиля.
        """
        return self.__num_doors

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля с дополнительным сообщением.

        :return: Сообщение о запуске двигателя с указанием типа автомобиля.
        """
        return f"{super().start_engine()} (Car)"

    def __str__(self) -> str:
        """Переопределение строкового представления для легкового автомобиля."""
        return f"{super().__str__()} with {self.__num_doors} doors"

    def __repr__(self) -> str:
        """Представление объекта для отладки легкового автомобиля."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, num_doors={self.__num_doors})"


# Пример использования классов
if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Camry", year=2020, num_doors=4)
    print(my_car)  # 2020 Toyota Camry with 4 doors
    print(repr(my_car))  # Car(make='Toyota', model='Camry', year=2020, num_doors=4)
    print(my_car.start_engine())  # Toyota Camry engine started. (Car)

