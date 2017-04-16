from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('X,Y,Z,A,B,C,D,E,F,baza,oblicz')

+baza('Nie musi pan placic podatku',0,3091,0,0,0)
+baza('Podatek dla pana wynosi 18%',3091,85528,0.18,556.02,0)
+baza('Podatek dla pana wynosi 32% dla kwoty powyżej 85528zł i 18% dla kwoty 85528zł',85528,1000000000,0.32,556.02,0)

oblicz(Z,X) <= baza(Z,A,B,C,D,E) & (X>A) & (X<=B) & (E=(X*C)-D)  # konkluzja <= przesłanki

print(oblicz(Z,4000))
