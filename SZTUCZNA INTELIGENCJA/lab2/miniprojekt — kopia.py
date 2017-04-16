from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('A,B,C,D,E,F,W,X,Y,procesor,karta,płyta,zestaw,oblicz,test')

#bazy danych
+procesor('Intel i7',2000)
+procesor('Intel i5',1200)
+procesor('Intel i3',700)
+procesor('Intel Pentium',500)
+procesor('Intel Celeron',300)

+karta('Geforce 1080',2000)
+karta('Geforce 1070',1700)
+karta('Geforce 1060',1200)
+karta('Geforce 1050',800)
+karta('Geforce 1040',500)
+karta('Geforce 1030',250)

+płyta('MSI',570)
+płyta('ASUS',400)
+płyta('Gigabyte',320)
+płyta('ChinaCD',120)

def zestaw1():
    y = str(input("Co ma byc najbardziej wydajne? (procesor,karta,plyta): "))
    X = int(input("Podaj swój fundusz który może przeznaczyć na komputer: "))
    if(X<=670):
        print("Masz za mało pieniążków")
    if(X<=4600 and X>670):
        if(y=='procesor'):
            oblicz(A,B,C,X) <= procesor(A,D) & karta(B,E) & płyta(C,F) & (D+E+F<X) & (D+E+F>X-400) & (D>0.4*X)
            print(oblicz(A,B,C,X))
        elif(y=='karta'):
            oblicz(A,B,C,X) <= procesor(A,D) & karta(B,E) & płyta(C,F) & (D+E+F<X) & (D+E+F>X-400) & (E>0.4*X)
            print(oblicz(A,B,C,X))
        elif(y=='plyta'):
            oblicz(A,B,C,X) <= procesor(A,D) & karta(B,E) & płyta(C,F) & (D+E+F<X) & (D+E+F>X-400) & (F>0.12*X)
            print(oblicz(A,B,C,X))
        else:
            print("Coś się popsuło nie rozpoznaje nazwy podzespołu")
    elif(X>4600):
        print("Stać Cię na wszystko")
        
    print("")
    z = str(input("Chcesz zaczac od poczatku(t/n): "))
    if(z=='t'):
        return zestaw1()


zestaw1()

#Program ten na podstawie preferencji danego podzespołu oraz kwoty jaką możemy
#wydać na zakupy wybierze nam zestaw komputerowy dopasowany do naszych potrzeb
#wersja ta jest oczywiście wersją dosyć okrojoną, ale dobrze ukazującą potencjał
#sztucznej inteligencji w pythonie
