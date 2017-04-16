class Bla:
    def wypisz(self):
        pass
    def __init__(self,x):
        self.x=x

a=Bla(4)
print(a.x)

# _x - zmienne prywatne
# __x - z - zmienna prywatna ale trudniejsza do zmiany, nie możemy jej zmienić w klasie

#class BLa(A,B,C) - dziedziczenie po klasie A B i C (wielodziedziczenie)
#A.__init__(self,x)
    #self.x=x
