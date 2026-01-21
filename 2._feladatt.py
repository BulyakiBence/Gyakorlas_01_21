"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon,
ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, 
és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
"""
import random
random_szamok = []
for num in range(10):
    random_szamok.append(random.randint(1,3))
print(random_szamok)    

torlendo = int(input("Adj meg egy számot [1;3] intervallumon: "))
random_szamok =  [szam for szam in random_szamok if szam != torlendo]
print(random_szamok)