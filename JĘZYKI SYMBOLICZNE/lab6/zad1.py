class Moneta:
    def __init__(self, x):
        y = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        if x not in y:
            x = 0
        self._x = x

    def wypisz(self):
        print(self._x)

    def get_x(self) -> int:
        return self._x
x=Moneta(70)
x.wypisz()
