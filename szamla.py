#Fájlbeolvasás(Dávid Marcell)

mobil=['39','41','71']
idok=[]
szamok=[]
db=0
with open('hivasok.txt') as fbe:
    for sor in fbe:
        if db%2==0:
            idok.append(sor.rstrip().split())
        else:
            szamok.append(sor)
        db+=1
print('Beolvasott adatok száma: %d\n' %(db//2))
for i in range(0,db//2):
    print(idok[i])
    print(szamok[i])


#1.Feladat(Kiss Kornél)
print('1. feladat')
def mobil_e(szam):
    igen=0
    if szam[0:2] in mobil:
        igen=1
    return igen
szam=str(input('Kérek egy telefonszámot: '))
if mobil_e(szam)==1:
    print('A megadott szám mobilszám!')
else:
    print('A megadott szám nem mobilszám!')




#2.Feladat(Dravicz Levente)





#3.Feladat(Dávid Marcell)






#4.Feladat(Dravicz Levente )






#5.Feladat(Kiss Kornél)






#6.Feladat(Dávid Marcell)