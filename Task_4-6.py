print('Задание 4.')


class Store:
    def __init__(self):
        """
        Список техники, поступившей на склад.
        """
        self.equipment = []

    def Accept(self):
        """
        Список техники заполняется словарем, включающим методы подклассов.
        :return: Функция возвращает готовый список.
        """
        self.equipment.append(dict(Принтер=Printer.Dictionary, Сканер=Scanner.Dictionary_2, Ксерокс=Xerox.Dictionary_3))
        return self.equipment


class OfficeEquipment:
    def __init__(self, brand, price, count):
        self.brand = brand
        self.price = price
        self.count = count


class Printer(OfficeEquipment):
    def __init__(self, ink_color, ink_value, brand, price, count):
        super().__init__(brand, price, count)
        self.ink_color = ink_color
        self.ink_value = ink_value
        self.parameter_1 = []

    def Dictionary(self):
        """
        Функция заполняет список parameter_1 словарем из параметров подкласса и отсекает некорректные данные.
        :return: Функция возвращает полученный словарь.
        """
        try:
            self.parameter_1.append(dict(Цвет_чернил=self.ink_color, Количество_чернил=int(self.ink_value),
                                         Марка=self.brand, Цена=int(self.price), Количество=int(self.count)))
        except ValueError:
            print('Данные для принтера введены некорректно!')
        return self.parameter_1


class Scanner(OfficeEquipment):
    def __init__(self, color, brand, price, count):
        super().__init__(brand, price, count)
        self.color = color
        self.parameter_2 = []

    def Dictionary_2(self):
        """
        Функция заполняет список parameter_2 словарем из параметров подкласса и отсекает некорректные данные.
        :return: Функция возвращает полученный словарь.
        """
        try:
            self.parameter_2.append(dict(Цвет_чернил=self.color, Марка=self.brand, Цена=int(self.price),
                                         Количество=int(self.count)))
        except ValueError:
            print('Данные для принтера введены некорректно!')
        return self.parameter_2


class Xerox(OfficeEquipment):
    def __init__(self, color, brand, price, count):
        super().__init__(brand, price, count)
        self.color = color
        self.parameter_3 = []

    def Dictionary_3(self):
        """
        Функция заполняет список parameter_3 словарем из параметров подкласса и отсекает некорректные данные.
        :return: Функция возвращает полученный словарь.
        """
        try:
            self.parameter_3.append(dict(Цвет_чернил=self.color, Марка=self.brand, Цена=int(self.price),
                                         Количество=int(self.count)))
        except ValueError:
            print('Данные для принтера введены некорректно!')
        return self.parameter_3


printer = Printer(input('Введите цвет чернил принтера: '), input('Введите количество чернил принтера, %: '),
                  input('Введите марку принтера: '), input('Введите цену принтера: '),
                  input('Введите количество единиц: '))
scanner = Scanner(input('Введите цвет сканера: '), input('Введите марку сканера: '),
                  input('Введите цену сканера: '), input('Введите количество единиц: '))
xerox = Xerox(input('Введите цвет чернил ксерокса: '), input('Введите марку ксерокса: '),
              input('Введите цену ксерокса: '), input('Введите количество единиц: '))
store = Store()
print(store.Accept())
print(printer.Dictionary())
print(scanner.Dictionary_2())
print(xerox.Dictionary_3())