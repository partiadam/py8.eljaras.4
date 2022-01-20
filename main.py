'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''

lista = []

beker1 = (input('Adj meg egy szót: \t'))
beker2 = (input('Adj meg egy szót: \t'))
beker3 = (input('Adj meg egy szót: \t'))

lista.append(beker1)
lista.append(beker2)
lista.append(beker3)

def legrovidebb():
    for i in range(1):
        print("A legrövidebb szó: ", min(lista, key=len))
legrovidebb()


