'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''

lista = []

for i in range(3):
    ker = input('Adj meg egy szót: \t')
    lista.append(ker)



def legrovidebb():
    [len(i) for i in lista]
    print(f"A legrövidebb szó: {min(lista)}")  
legrovidebb()