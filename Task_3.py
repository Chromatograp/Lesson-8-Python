print('Задание 3.')


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NumberList:

    @property
    def List(self):
        my_list = []
        try:
            while True:
                num = input('Введите числа, разделяя их пробелом: ')
                for i in num.split():
                    if int(i) < 0:
                        raise OwnError('Вводить только положительные числа!')
                    my_list.append(int(i))
                if input('Продолжить? да/нет ') == 'нет':
                    break
        except ValueError:
            print('Вводить только числа!')
        except OwnError as error:
            print(error)
        else:
            print('Ввод корректен.')
        finally:
            print('Программа завершена.')
        return my_list


nl=NumberList()
print(f'Введенный вами список {nl.List}')