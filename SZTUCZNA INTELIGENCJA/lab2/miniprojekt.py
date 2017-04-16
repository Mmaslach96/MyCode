from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('A,B,C,D,E,F,W,X,Y,Z,Q,G,procesor,karta,płyta,xprocesor,ykarta,zpłyta,oblicz,sprawdz,odp,oblicz,odp1,zestaw')

#bazy danych
+procesor('Intel i7',2000,"bardzo dobry")
+procesor('Intel i5',1200,"bardzo dobry")
+procesor('Intel i3',700,"dobry")
+procesor('Intel Pentium',500,"słaby")
+procesor('Intel Celeron',300,"bardzo słaby")

+karta('Geforce 1080',2000,"bardzo dobra")
+karta('Geforce 1070',1700,"bardzo dobra")
+karta('Geforce 1060',1200,"mocna")
+karta('Geforce 1050',800,"średnia")
+karta('Geforce 1040',500,"słaba")
+karta('Geforce 1030',250,"bardzo słaba")

+płyta('MSI',570,"bardzo dobra")
+płyta('ASUS',400,"dobra")
+płyta('Gigabyte',320,"dobra")
+płyta('ChinaCD',120,"słaba")

+odp("Twój komp jest najlepszy na rynku!",4500,10000)
+odp("Jest moc!",3800,4500)
+odp("Jest dobry",3200,3800)
+odp("No tak średnio bym powiedział",2500,3200)
+odp("Przeciętniak!",1700,2500)
+odp("Chyba masz z nim problemy co?",1300,1700)
+odp("To w ogóle działa??!",0,1300)

+odp1("Tak pasuje",-500,500)
+odp1("Nie nie pasuje",500,4000)
+odp1("Nie nie pasuje",-4000,-500)


#reguły
xprocesor(X,C) <= procesor(X,B,C)
ykarta(Y,C) <= karta(Y,B,C)
zpłyta(Z,C) <= płyta(Z,B,C)
sprawdz(X,Y,Z,Q) <= procesor(X,A,D) & karta(Y,B,E) & płyta(Z,C,F) & odp(Q,W,G) & (A+B+C>W) & (A+B+C<=G)
zestaw(X,Y,Z,Q) <= procesor(X,A,D) & karta(Y,B,E) & płyta(Z,C,F) & (A+B+C<Q) & (A+B+C>=Q-500)
oblicz(X,Y,Z,Q) <= procesor(X,A,D) & karta(Y,B,E) & płyta(Z,C,F) & odp1(Q,W,G) & (A-B>W) & (A-B<=G)

#dialog i wyciąganie wniosków na podstawie reguł(wymagane jest podawanie danych z bazy)
print("Czesc porozmawiajmy o Twoim komputerze")
X=str(input("Podaj mi nazwe swojego procesora: "))
print(xprocesor(X,C))

Y=str(input("Podaj mi nazwe swojej karty: "))
print(ykarta(Y,C))

Z=str(input("Podaj mi nazwe swojej płyty głównej: "))
print(zpłyta(Z,C))

print("A teraz powiem Ci jak oceniam Twój komputer: ")
print(sprawdz(X,Y,Z,C))

print("Sprawdze czy procesor pasuje do karty: ")
print(oblicz(X,Y,Z,C))

Q=int(input("Mozesz teraz podac kwote a ja Ci zaproponuje jakieś zestawy: "))
print(zestaw(A,B,D,Q))









