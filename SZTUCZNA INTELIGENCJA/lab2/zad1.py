from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('X,Y,Z,A,B,mezczyzna, kobieta, rodzice, rlubi, lubi, alkohol, sok, rodzenstwo')

#bazy danych
+mezczyzna('Adam')
+mezczyzna('Stefan')
+mezczyzna('Staszek')
+mezczyzna('Marek')

+kobieta('Alicja')
+kobieta('Alina')
+kobieta('Maria')
+kobieta('Anna')

+lubi('Wojtek','piwo')
+lubi('Magda','sok')
+lubi('Eliza','piwo')
+lubi('Jan','sok')

# rodzice(x,y,z) x:potomek, y:ojciec, z:matka
+rodzice('Stefan', 'Staszek', 'Maria')
+rodzice('Alicja', 'Staszek', 'Maria')
+rodzice('Anna', 'Marek', 'Alina')

#wyszukanie rodzicow stefana
print(rodzice('Stefan',X,Y))
#wyszukanie dzieci i żony Staszka
print(rodzice(X,'Staszek',Y))

#regula sprawdzający czy dwie osoby są rodzeństwem
rodzenstwo(Y, X) <= rodzice(Y,A,B) & rodzice(X,A,B) # konkluzja <= przesłanki

#sprawdzenie czy Stefan i Alicja sa rodzenstwem(output true or false)
print(rodzenstwo('Stefan','Alicja'))

#regula że ktoś lubi piwo
rlubi(Y, X) <= lubi(X,'piwo')  # konkluzja <= przesłanki

#wywolanie że Stefan lubi osoby któe lubią piwo
print(rlubi('Stefan', X))
