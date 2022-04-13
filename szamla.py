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
print("2. feladat'')
def percek(idoadat): 
   
    kezdes=int(idoadat[0])*3600+int(idoadat[1])*60+int(idoadat[2])

    vege=int(idoadat[3])*3600+int(idoadat[4])*60+int(idoadat[5])

    perc=(vege-kezdes)//60

    if (vege-kezdes)%60!=0:
        perc+=1
    return perc
idoadat=[]
szoveg=['Kezdés óra: ','Kezdés perc: ','Kezdés másodperc: ','Vége óra: ','Vége perc: ','Vége másodperc: ']
for i in range(0,6):
    inp=str(input(szoveg[i]))
    idoadat.append(inp)
print(idoadat)
ki=percek(idoadat)
print('A hívás ideje: %d perc\n' %(ki))




#3.Feladat(Dávid Marcell)






#4.Feladat(Dravicz Levente )






#5.Feladat(Kiss Kornél)






#6.Feladat(Dávid Marcell)