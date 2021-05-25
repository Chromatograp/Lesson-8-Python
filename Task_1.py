print('Задание 1.')


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def Method(cls, data):
        try:
            date = []
            for i in data.split('-'):
                date.append(int(i))
            return date
        except ValueError:
            print('Дата введена некорректно!')

    @staticmethod
    def Validation(Method):
        if Method[0] > 31:
            print('В месяце меньше дней!')
        elif Method[1] > 12:
            print('В году меньше месяцев!')
        else:
            pass


print(Data.Method(input('Введите дату: ')))
print(Data.Validation(Data.Method))
# data=Data(input('Введите дату: '))
# print(data.Method(input('Введите дату: ')))

