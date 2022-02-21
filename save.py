naplo = {}
diak = []
with open('naplo.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        if sor[0] == '#':
            datum_sor = sor.strip().split()
            datum = datum_sor[1] + ' ' + datum_sor[2]
            naplo[datum] = []
        else:
            bejegyzes = sor.strip().split()
            naplo[datum].append([item for item in bejegyzes])


def hetnapja(honap, nap):
    napnev = ['vasarnap', 'hetfo', 'kedd', 'szerda', 'csutortok', 'pentek', 'szombat']
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]


print('6. feladat')
nap_neve = input('A nap neve: ')
ora = int(input('Add meg az ora szamat: '))
hianyzas = 0

for datum in naplo:
    if hetnapja(int(datum[:2]), int(datum[3:])) == nap_neve:
        for bejegyzes in naplo[datum]:
            if 'X' == bejegyzes[-1][ora - 1] or 'I' == bejegyzes[-1][ora - 1]:
                hianyzas += 1
print(hianyzas)