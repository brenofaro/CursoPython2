# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        valor_x = self.x + other.x
        valor_y = self.y + other.y
        return Ponto(valor_x, valor_y)

    def __gt__(self, other) -> bool:
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y

        if (resultado_self) > (resultado_other):
            return True
        else:
            return False


if __name__ == '__main__':
    p1 = Ponto(2, 3)
    p2 = Ponto(9, 7)
    p3 = p1 + p2
    print(p3)
    print("P1 é maior que p2", p1 > p2)
    print("P2 é maior que p1", p2 > p1)
