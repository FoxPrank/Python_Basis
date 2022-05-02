# 1
class Matrix:
    def __init__(self,data):
        self.data = data

    def __str__(self):
        res = '\n'.join(str(el) for el in self.data)
        return res
    def __add__(self, other):
        matr_row = len(self.data)
        matr_shape = len(self.data[0])
        res = [[self.data[i][j] + other.data[i][j] for j in range(matr_shape)] for i in range(matr_row)]
        return Matrix(res)

mm = Matrix([[1,2],[3,4]])
mm2 = Matrix([[1,1],[1,1]])
mm3 = mm + mm2
print(mm3)
# как добиться вывода без скобок я не понимаю, по идее, если в обычном цикле для списка списков у меня получалось
# через map(str, el) - повторить с выводом сразу так и не получилось.
# Если есть возможность, скиньте, пжл, пояснения как решать.
# 2
class Clothes:
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    def __init__(self, name, v):
        super(Coat, self).__init__(name)
        self.v = v
    def coat_cloth_cons(self):
        res = round(self.v/6.5 +0.5,5)
        return f'{res} м. ткани требуется для изготовления пальто: {self.name}'

class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def suit_cloth_cons(self):
        res = round(self.h*2 + 0.3,3)
        return res

cc = Coat("Драповое",8)
print(cc.coat_cloth_cons())

ss = Suit("Мужской", 180)
print(ss.suit_cloth_cons())
# 3
class Cell:
    def __init__(self,qty):
        self.q = int(qty)
    def __str__(self):
        return f'Cell qty: {self.q}'
    def __add__(self, other):
        return Cell(self.q + other.q)
    def __sub__(self, other):
        if self.q - other.q > 0:
            return Cell(self.q - other.q)
        else:
            print('Вычетание невозможно, ответ отрицательный')
    def __mul__(self, other):
        return Cell(self.q * other.q)
    def __truediv__(self, other):
        return Cell(self.q //other.q)
    def make_order(self, q_in_row):
        _fstr = ''
        for i in range(self.q // q_in_row):
            _fstr += f'{"*" * q_in_row}\n'
        _fstr += f'{"*"*(self.q % q_in_row)}'
        return _fstr
cc = Cell(12)
cc2 = Cell(5)
fff = cc + cc2
print(fff)
print(cc - cc2)
print(cc2 - cc)
print(cc * cc2)
print(cc/cc2)
print(cc.make_order(5))

