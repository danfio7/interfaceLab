def stampaDizionario(diz):
    for key,value in diz.items():
        print("la chiave è ..."+key)
        print("il valore è ..."+str(value))

def totaleOre(diz):
    somma=0
    for key,value in dizionario.items():
        somma+=value
    return somma

def numeroCattedrePiene(diz):
    insegnantiPieni=0
    for key,value in dizionario.items():
        if value==18:
            insegnantiPieni+=1 
    return insegnantiPieni

def allocaOre(diz,nome,ore):
    if nome in diz:
        diz[nome]=ore
    return dizionario
somma=0
def scalaOre(diz,nome,ore):
    if nome in diz:
        if diz[nome] > ore:
            diz[nome]-=ore
    return somma
   

dizionario = {"rossi":18, "bianchi":16, "verdi":6 }
#inserire un elemento dentro un dizionario
dizionario["viola"]=14
print(dizionario)
#modificare una coppia chiave valore
dizionario["bianchi"]=18
print(dizionario)

stampaDizionario(dizionario)

#itereare sul dizionario
for key,value in dizionario.items():
    print("la chiave è ..."+key)
    print("il valore è ..."+str(value))

#calcolare il totale delle ore del dizionario
somma=0
for key,value in dizionario.items():
    somma+=value
print(somma)

#numero degli insegnanti con cattedra piena
insegnantiPieni=0
for key,value in dizionario.items():
    if value==18:
        insegnantiPieni+=1 
print(insegnantiPieni)

allocaOre(dizionario, "bianchi", 10)
print(dizionario)

scalaOre(dizionario,"bianchi",5)
print(dizionario)