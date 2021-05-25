print('Задание 2.')


class Divide:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __truediv__(self):
        try:
            return self.number_1 / self.number_2
        except ZeroDivisionError:
            print('На ноль делить нельзя!')


divide=Divide(int(input('Введите числитель: ')), int(input('Введите знаменатель: ')))
print(f'{divide.number_1}/{divide.number_2} =', divide.__truediv__())
