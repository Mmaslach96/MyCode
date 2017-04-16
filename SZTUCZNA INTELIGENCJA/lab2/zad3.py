from pyDatalog import pyDatalog as pl

#zmienne
pl.create_terms('X,Y,Z,A,B,baza,oblicz')

+baza('Nie musi pan placic podatku',0,3091)
+baza('Podatek dla pana wynosi 18%',3091,85528)
+baza('Podatek dla pana wynosi 32% dla kwoty powyżej 85528zł i 18% dla kwoty 85528zł',85528,1000000000)

oblicz(Z,X) <= baza(Z,A,B) & (X>A) & (X<=B) # konkluzja <= przesłanki

#funkcja na przedzial podatkowy
def podatek(X):
    oblicz(Z,X) <= baza(Z,A,B) & (X>A) & (X<=B) # konkluzja <= przesłanki
    if(X<=3091): #przypadek bez podatku
        print(oblicz(Z,X))
    elif(X>3091 and X<=85528): #stawka 18%
        print(oblicz(Z,X))
        print('Który wynosi: ', (X*0.18)-556.02)
    elif(X>85528): #stawka 18% do 85528 i 32% dla powyżej
        print(oblicz(Z,X))
        print('Który wynosi: ', ((85528*0.18)-556.02)+((X-85528)*0.32))
        
podatek(85628) #wywolanie funkcji

