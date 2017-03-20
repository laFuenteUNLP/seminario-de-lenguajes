#!/usr/bin/python
# coding=utf-8

'''
Dado el siguiente diccionario donde las claves son nombres de animales y los valores representan
posiciones:
anim={’Gato Montes’:2,’Yacare overo’:4,’Boa acuática’:5}
Imprimir un string por cada animal de la estructura, reemplazando sus caracteres por el string
’_ ’ (inclusive los espacios en blanco) salvo el caracter correspondiente al valor del mismo.
Ejemplo: Gato Montes tiene asociado el valor 2:
_ _ t _ _ _ _ _ _ _ _
0 1 2 3 4 5 6 7 8 9 10
'''

anim={'Gato Montes':2,'Yacare overo':4,'Boa acuatica':5}

for a in anim:
    aux = a[anim[a]]
    news = ""
    i=0
    for c in a:
        if i == anim[a]:
            newc = a[anim[a]]
        else:
            newc = c.replace(c, "_ ")
        news = news + newc
        i = i + 1
    newl = []
    newl.append(news)
    anim[a] =  news

print anim
