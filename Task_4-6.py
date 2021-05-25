print('Задание 4.')


class Store:

class OfficeEquipment:
    def __init__(self, brand, price, year):
        self.brand=brand
        self.price=price
        self.year=year

    def Acceptance(self):
        product_list = []
        i = 1
        while True:
            product_list.append((input('Введите номер товара: '), dict(dict(class = (input('Введите наименование: ')),
            self.brand = (input('Введите марку: ')), self.year = int(input('Введите год выпуска: ')),
            self.price = int(input('Введите цену: '))))))
            if input('Товар добавлен. Добавить еще один? да/нет ') == 'нет':
                break
        i += 1

class Printer(OfficeEquipment):
    def __init__(self, ink_color, ink_value, brand, price, year):
        super().__init__(brand, price, year)
        self.ink_color=ink_color
        self.ink_value=ink_value

class Scanner(OfficeEquipment):
    def __init__(self, color, brand, price, year):
        super().__init__(brand, price, year)
        self.color=color

class Xerox(OfficeEquipment):
    def __init__(self, color, brand, price, year):
        super().__init__(brand, price, year)
        self.color=color