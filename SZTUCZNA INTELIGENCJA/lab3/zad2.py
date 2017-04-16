import pymc
import numpy as np
import pandas as pd


zabiłA = pymc.Bernoulli('zabiłA', .33, value=np.ones(1))

zabiłB = pymc.Bernoulli('zabiłB', .33, value=np.ones(1))

zabiłC = pymc.Bernoulli('zabiłC', .33, value=np.ones(1))



p_odciskiA = pymc.Lambda('p_odciskiA', lambda zabiłA=zabiłA, : np.where(zabiłA, .7, .5))
odciskiA = pymc.Bernoulli('odciskiA', p_odciskiA, value=np.ones(1))

p_niealibiA = pymc.Lambda('p_niealibiA', lambda zabiłA=zabiłA: np.where(zabiłA, .9, .5))
niealibiA = pymc.Bernoulli('niealibiA', p_niealibiA, value=np.ones(1))

p_motywA = pymc.Lambda('p_motywA', lambda zabiłA=zabiłA: np.where(zabiłA, .6, .5))
motywA = pymc.Bernoulli('motywA', p_motywA, value=np.ones(1))

p_złyrysopisA = pymc.Lambda('p_złyrysopisA', lambda zabiłA=zabiłA: np.where(zabiłA, .2,.5))
złyrysopisA = pymc.Bernoulli('złyrysopisA', p_złyrysopisA, value=np.ones(1))

p_szanowanyA = pymc.Lambda('p_szanowanyA', lambda zabiłA=zabiłA: np.where(zabiłA, .3, .5))
szanowanyA = pymc.Bernoulli('szanowanyA', p_szanowanyA, value=np.ones(1))




p_odciskiB = pymc.Lambda('p_odciskiB', lambda zabiłB=zabiłB, : np.where(zabiłB, .7, .5))
odciskiB = pymc.Bernoulli('odciskiB', p_odciskiB, value=np.ones(1))

p_niealibiB = pymc.Lambda('p_niealibiB', lambda zabiłB=zabiłB: np.where(zabiłB, .9, .5))
niealibiB = pymc.Bernoulli('niealibiB', p_niealibiB, value=np.ones(1))

p_motywB = pymc.Lambda('p_motywB', lambda zabiłB=zabiłB: np.where(zabiłB, .6, .5))
motywB = pymc.Bernoulli('motywB', p_motywB, value=np.ones(1))

p_złyrysopisB = pymc.Lambda('p_złyrysopisB', lambda zabiłB=zabiłB: np.where(zabiłB, .2, .5))
złyrysopisB = pymc.Bernoulli('złyrysopisB', p_złyrysopisB, value=np.ones(1))

p_szanowanyB = pymc.Lambda('p_szanowanyB', lambda zabiłB=zabiłB: np.where(zabiłB, .3, .5))
szanowanyB = pymc.Bernoulli('szanowanyB', p_szanowanyB, value=np.ones(1))





p_odciskiC = pymc.Lambda('p_odciskiC', lambda zabiłC=zabiłC, : np.where(zabiłC, .7, .5))
odciskiC = pymc.Bernoulli('odciskiC', p_odciskiC, value=np.ones(1))

p_niealibiC = pymc.Lambda('p_niealibiC', lambda zabiłC=zabiłC: np.where(zabiłC, .9, .5))
niealibiC = pymc.Bernoulli('niealibiC', p_niealibiC, value=np.ones(1))

p_motywC = pymc.Lambda('p_motywC', lambda zabiłC=zabiłC: np.where(zabiłC, .6, .5))
motywC = pymc.Bernoulli('motywC', p_motywC, value=np.ones(1))

p_złyrysopisC = pymc.Lambda('p_złyrysopisC', lambda zabiłC=zabiłC: np.where(zabiłC, .2, .5))
złyrysopisC = pymc.Bernoulli('złyrysopisC', p_złyrysopisC, value=np.ones(1))

p_szanowanyC = pymc.Lambda('p_szanowanyC', lambda zabiłC=zabiłC: np.where(zabiłC, .3, .5))
szanowanyC = pymc.Bernoulli('szanowanyC', p_szanowanyC, value=np.ones(1))



# model
model = pymc.Model([p_odciskiA, odciskiA, p_niealibiA, niealibiA, p_motywA, motywA, p_złyrysopisA, szanowanyA, p_szanowanyA, złyrysopisA,    p_odciskiB, odciskiB, p_niealibiB, niealibiB, p_motywB, motywB, p_złyrysopisB, szanowanyB, p_szanowanyB, złyrysopisB,    p_odciskiC, odciskiC, p_niealibiC, niealibiC, p_motywC, motywC, p_złyrysopisC, szanowanyC, p_szanowanyC, złyrysopisC, zabiłA, zabiłB, zabiłC])

mcmc = pymc.MCMC(model)
mcmc.sample(10000,2000)

# wyciągnięcie scieżek dla każdej ze zmiennych
t_zabiłA = mcmc.trace('zabiłA')[:]
t_zabiłB = mcmc.trace('zabiłB')[:]
t_zabiłC = mcmc.trace('zabiłC')[:]
t_odciskiA = mcmc.trace('odciskiA')[:]
t_niealibiA = mcmc.trace('niealibiA')[:]
t_motywA = mcmc.trace('motywA')[:]
t_złyrysopisA = mcmc.trace('złyrysopisA')[:]
t_szanowanyA = mcmc.trace('szanowanyA')[:]
t_odciskiB = mcmc.trace('odciskiB')[:]
t_niealibiB = mcmc.trace('niealibiB')[:]
t_motywB = mcmc.trace('motywB')[:]
t_złyrysopisB = mcmc.trace('złyrysopisB')[:]
t_szanowanyB = mcmc.trace('szanowanyB')[:]
t_odciskiC = mcmc.trace('odciskiC')[:]
t_niealibiC = mcmc.trace('niealibiC')[:]
t_motywC = mcmc.trace('motywC')[:]
t_złyrysopisC = mcmc.trace('złyrysopisC')[:]
t_szanowanyC = mcmc.trace('szanowanyC')[:]

# stworzenie słownika, zamieniamy wartości logiczne True/False na 1/0
dictionary = {
              'zabiłA': [1 if ii[0] else 0 for ii in t_zabiłA.tolist() ],
              'zabiłB': [1 if ii[0] else 0 for ii in t_zabiłB.tolist() ],
              'zabiłC': [1 if ii[0] else 0 for ii in t_zabiłC.tolist() ],
              'odciskiA': [1 if ii[0] else 0 for ii in t_odciskiA.tolist() ],
              'niealibiA': [1 if ii[0] else 0 for ii in t_niealibiA.tolist()],
              'motywA': [1 if ii[0] else 0 for ii in t_motywA.tolist()],
              'złyrysopisA': [1 if ii[0] else 0 for ii in t_złyrysopisA.tolist()],
              'szanowanyA': [1 if ii[0] else 0 for ii in t_szanowanyA.tolist()],
              'odciskiB': [1 if ii[0] else 0 for ii in t_odciskiB.tolist() ],
              'niealibiB': [1 if ii[0] else 0 for ii in t_niealibiB.tolist()],
              'motywB': [1 if ii[0] else 0 for ii in t_motywB.tolist()],
              'złyrysopisB': [1 if ii[0] else 0 for ii in t_złyrysopisB.tolist()],
              'szanowanyB': [1 if ii[0] else 0 for ii in t_szanowanyB.tolist()],
              'odciskiC': [1 if ii[0] else 0 for ii in t_odciskiC.tolist() ],
              'niealibiC': [1 if ii[0] else 0 for ii in t_niealibiC.tolist()],
              'motywC': [1 if ii[0] else 0 for ii in t_motywC.tolist()],
              'złyrysopisC': [1 if ii[0] else 0 for ii in t_złyrysopisC.tolist()],
              'szanowanyC': [1 if ii[0] else 0 for ii in t_szanowanyC.tolist()],
              }
# stworzenie obiektu DataFrame
df = pd.DataFrame(dictionary)
# podgląd tabeli (pierwsze 5 wierszy)
print(df.head())

#praawdopodobieństwo że zabił A z uwzględnieniem że jest szanowany i nie miał alibi
pA = float(df[(df['zabiłA'] == 1) & (df['szanowanyA'] == 1) & (df['niealibiA'] == 1)].shape[0])/ df[(df['szanowanyA'] == 1) & (df['niealibiA'] == 1) ].shape[0]
print('p_zabiłA:', pA)
#praawoopodobieństwo że zabił B z uwzględnieniem że rysopis nie pasuje i nie ma alibi
pB = float(df[(df['zabiłB'] == 1) & (df['złyrysopisB'] == 1) & (df['niealibiB'] == 1)].shape[0])/ df[(df['złyrysopisB'] == 1) & (df['niealibiB'] == 1) ].shape[0]
print('p_zabiłB:', pB)
#praawdopodobieństwo że zabił C z uwzględnieniem że że rysopis nie pasuje i miał motyw
pC = float(df[(df['zabiłC'] == 1) & (df['złyrysopisC'] == 1) & (df['motywC'] == 1)].shape[0])/ df[(df['złyrysopisC'] == 1) & (df['motywC'] == 1) ].shape[0]
print('p_zabiłC:', pC)

# następnie dzielimy każde p przez sume p zgodnie ze wzorem ze skryptu p=pX/(pX+pY+....)
A = pA/(pA+pB+pC)
B = pB/(pA+pB+pC)
C = pC/(pA+pB+pC)

print("Praawdopodobieństwo że zabił A: ",A)
print("Praawdopodobieństwo że zabił B: ",B)
print("Praawdopodobieństwo że zabił C: ",C)
#z tego wynika że zabił A z p = 42.9%

#z tego wynika że całkowite praawdopodobieństwo czyli suma pA+pB+pC=1 czyli wszytsko się zgadza
print("Praawdopodobieństwo że zabił A lub B lub C",A+B+C)
