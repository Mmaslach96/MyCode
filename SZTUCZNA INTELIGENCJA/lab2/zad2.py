from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('krol,rzadzil,X,Y,Z,A,B')

#baza danych
+krol('Mieszko1',960,992)
+krol('Bolesław1',992,1025)
+krol('Mieszko2',1025,1031)
+krol('Bezprym',1031,1032)
+krol('Mieszko2',1033,1034)
+krol('Kazimierz1',1034,1058)
+krol('Bolesław2',1058,1079)
+krol('Władysław1',1079,1086)

#regula na znalezienie króla panującego w danym roku
rzadzil(X, Y) <= krol(X,A,B) & (Y>=A) & (Y<=B) # konkluzja <= przesłanki

#wywolanie króli którzy rządzili w 1034r
print(rzadzil(X,1034))
