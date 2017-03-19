#!/usr/bin/python
# coding=utf-8

'''
Dada la estructura del ejercicio 7, ingresar los datos correspondientes a la jugada de un usuario.
Si el usuario existe previamente, guardar los datos de mayor puntaje.
Luego imprimir el ranking de los 10 mejores puntajes.
'''

jugadores = []


while True :
	nombreaux = raw_input("Ingrese nombre de su Jugador: ")
	if nombreaux == "0000":
		break
	nivelaux = raw_input("Ingrese nivel de su Jugador: ")
	puntajemaxaux = raw_input("Ingrese puntaje máximo de su Jugador:")
	tiempoaux = raw_input("Ingrese tiempo jugado: ")
	jugador = { 'nombre': nombreaux, 'nivel': nivelaux, 'puntajemax': puntajemaxaux, 'tiempo': tiempoaux }

	print("Se creó un nuevo jugador con nombre %s nivel %s puntaje máximo %s y tiempo jugado %s" % (jugador['nombre'], jugador['nivel'], jugador['puntajemax'], jugador['tiempo']))
	jugadores.append(jugador)

for j in jugadores:
	print("Jugador: %s" % (j['nombre']))

jugador_jugada = raw_input("Ingrese nombre del Jugador de la jugada: ")
puntaje_jugada = raw_input("Ingrese puntaje de la jugada de %s:" % (jugador_jugada))

for j in jugadores:
	if j['nombre'] == jugador_jugada:
		j['puntajemax'] = max(int(j['puntajemax']), int(puntaje_jugada))

#bubblesort
def  ordenar_burbuja(L):
	for i in range(1,len(L)):
		for j in range(0, len(L)-i):
			if int(L[j]['puntajemax']) < int(L[j+1]['puntajemax']):
				temp=L[j]
				L[j]=L[j+1]
				L[j+1]=temp
	return L

top10 = ordenar_burbuja(jugadores)[:10]
print('Top 10 mejores puntajes')
for j in top10:
	print("Jugador: %s Puntaje: %s" % (j['nombre'], j['puntajemax']))
