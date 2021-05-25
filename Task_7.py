print('Задание 7.')


class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self):
        return self.num_1 + self.num_2

    def __mul__(self):
        return self.num_1 * self.num_2


cn=ComplexNumber(complex(2, 8), complex(3, 7))
print(f'{cn.num_1}+{cn.num_2}={cn.__add__()}')
print(f'{cn.num_1}*{cn.num_2}={cn.__mul__()}')