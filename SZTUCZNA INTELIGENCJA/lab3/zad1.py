import pymc
import numpy as np
import pandas as pd

# prawd. że zabił
zabił = pymc.Bernoulli('zabił', .5, value=np.ones(1))

# prawd. że zabił pod warunkiem że były odciski
p_odciski = pymc.Lambda('p_odciski', lambda zabił=zabił: np.where(zabił, .7, .3))
odciski = pymc.Bernoulli('odciski', p_odciski, value=np.ones(1))

# prawd. że zabił pod warunkiem że nie ma alibi
p_niealibi = pymc.Lambda('p_niealibi', lambda zabił=zabił: np.where(zabił, .8, .4))
niealibi = pymc.Bernoulli('niealibi', p_niealibi, value=np.ones(1))

# prawd. że zabił pod warunkiem że miał motyw
p_motyw = pymc.Lambda('p_motyw', lambda zabił=zabił: np.where(zabił, .9, .5))
motyw = pymc.Bernoulli('motyw', p_motyw, value=np.ones(1))

# prawd. że zabił pod warunkiem że był widziany w okolicy gdzie widywany jest dealer
p_widziany = pymc.Lambda('p_widziany', lambda zabił=zabił: np.where(zabił, .4, .2))
widziany = pymc.Bernoulli('widziany', p_widziany, value=np.ones(1))

# prawd. że zabił pod warunkiem że rysopis się nie zgadza
p_złyrysopis = pymc.Lambda('p_złyrysopis', lambda zabił=zabił: np.where(zabił, .2, .4))
złyrysopis = pymc.Bernoulli('złyrysopis', p_złyrysopis, value=np.ones(1))

# model
model = pymc.Model([p_odciski, odciski, p_niealibi, niealibi, p_motyw, motyw, p_widziany, widziany, p_złyrysopis, złyrysopis, zabił])

# im więcej iteracji tym lepsze oszacowania ale dłuższy czas wykonania
mcmc = pymc.MCMC(model)
mcmc.sample(10000,2000)

# wyciągnięcie scieżek dla każdej ze zmiennych
t_zabił = mcmc.trace('zabił')[:]
t_odciski = mcmc.trace('odciski')[:]
t_niealibi = mcmc.trace('niealibi')[:]
t_motyw = mcmc.trace('motyw')[:]
t_widziany = mcmc.trace('widziany')[:]
t_złyrysopis = mcmc.trace('złyrysopis')[:]

# stworzenie słownika, zamieniamy wartości logiczne True/False na 1/0
dictionary = {
              'zabił': [1 if ii[0] else 0 for ii in t_zabił.tolist() ],
              'odciski': [1 if ii[0] else 0 for ii in t_odciski.tolist() ],
              'niealibi': [1 if ii[0] else 0 for ii in t_niealibi.tolist()],
              'motyw': [1 if ii[0] else 0 for ii in t_motyw.tolist()],
              'widziany': [1 if ii[0] else 0 for ii in t_widziany.tolist()],
              'złyrysopis': [1 if ii[0] else 0 for ii in t_złyrysopis.tolist()],
              }
# stworzenie obiektu DataFrame
df = pd.DataFrame(dictionary)
# podgląd tabeli (pierwsze 5 wierszy)
print(df.head())

#gdyby znaleziono na miejscu zbrodni jego odciski palców 0.702228
p_zabił_odciski = float(df[(df['zabił'] == 1) & (df['odciski'] == 1)].shape[0]) / df[df['odciski'] == 1].shape[0]
print('p_zabił_odciski:', p_zabił_odciski)

#gdyby stwierdzono, że nie miał alibi i miał motyw 0.79022
p_zabił_niealibi_motyw = float(df[(df['zabił'] == 1) & (df['niealibi'] == 1) & (df['motyw'] == 1)].shape[0]) / df[(df['niealibi'] == 1) & (df['motyw'] == 1)].shape[0]
print('p_zabił_niealibi_motyw:', p_zabił_niealibi_motyw)

#gdyby znaleziono na miejscu zbrodni jego odciski palców oraz stwierdzono, że był widziany w sąsiedztwie miejsca, w którym mieszka nielegalny handlarz bronią, ale świadek zbrodni podał rysopis zabójcy nie pasujący do głównego podejrzanego 0.7147
p_zabił_odciski_widziany_złyrysopis = float(df[(df['zabił'] == 1) & (df['odciski'] == 1) & (df['widziany'] == 1) & (df['złyrysopis'] == 1)].shape[0]) / df[(df['odciski'] == 1) & (df['widziany'] == 1) & (df['złyrysopis'] == 1)].shape[0]
print('p_zabił_odciski_widziany_złyrysopis:', p_zabił_odciski_widziany_złyrysopis)

# w przypadku gdyby nie miał alibi i miał motyw ~79%