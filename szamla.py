#Fájlbeolvasás(Dávid Marcell)

idok=[]
szamok=[]
db=0

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
def percek(idoadat): 




#3.Feladat(Dávid Marcell)






#4.Feladat(Dravicz Levente )






#5.Feladat(Kiss Kornél)


print('5. feladat')
perc_m=0
perc_v=0
for i in range(0,db//2):
    if mobil_e(szamok[i])==1:
        perc_m+=percek(idok[i])
    else:
        perc_v+=percek(idok[i])
       
print('Mobil hívások ideje:  %d perc' %(perc_m))
print('Vezetékes hívások ideje: %d perc\n' %(db_csk))



#6.Feladat(Dávid Marcell)