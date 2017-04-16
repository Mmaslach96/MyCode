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


class Skarbonka:
    def __init__(self):
        self._coins = []

    def dodaj(self, c):
        if isinstance(c, Moneta):
            self._coins.append(c)
        else:
            print("Przesłany obiekt nie jest monetą.")

    def get_balance(self) -> int:
        bal = 0
        for c in self._coins:
            bal += c.get_x()
        return bal
        



y=Skarbonka()
y.dodaj(Moneta(5))
y.dodaj(Moneta(3))
y.dodaj(Moneta(2))
y.dodaj(Moneta(0))

print(y.get_balance())


        
