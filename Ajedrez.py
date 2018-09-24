#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
from Tkinter import * #Para evitar el main
from Graphics import * 
import subprocess
import platform
import shutil
import random


def get_caminos (status, lectura):
		if (lectura == 'r' or lectura == 'R'):

			if(status == '1'):
				return ['2', '4']

			elif(status == '2'):
				return ['4', '6']

			elif(status == '3'):
				return ['2', '6']

			elif status == '4':
				return ['2', '8']

			elif status == '5':
				return ['2', '4', '6', '8']

			elif status == '6':
				return ['2', '8']

			elif status == '7':
				return ['4', '8']

			elif status == '8':
				return ['4', '6']

			elif status == '9':
				return ['6', '8']


		elif lectura == 'b' or lectura == 'B':

			if(status == '1'):
				return ['5']

			elif (status == '2'):
				return ['1', '3', '5']

			elif (status == '3'):
				return ['5']

			elif (status == '4'):
				return ['1', '5', '7']

			elif (status == '5'):
				return ['1', '3', '7', '9']

			elif (status == '6'):
				return ['3', '5', '9']

			elif (status == '7'):
				return ['5']

			elif (status == '8'):
				return ['5', '7', '9']

			elif (status == '9'):
				return ['5']


		else:
			return['-1', '-2'] #Es decir si se encuentra una cadena que no sea r o b 

def generar_cadena():

	tam = random.randint(1, 10)
	cadena = ""

	for i in range(0, tam):

		opc = random.randint(0,1)
		if(opc):
			cadena += "r"
		else:
			cadena += "b"

	return cadena

def tablero (mostrar):

	#Crear ventana 
	tablero = GraphWin("tablero", 300,350)
	tablero.setBackground("black")

	Marco = Rectangle(Point(35,35), Point(255, 255))
	Marco.setFill(color_rgb(255, 59, 48))
	Marco.draw(tablero)

	b1 = Rectangle(Point(40, 40), Point(110,110))
	b1.setFill(color_rgb(255, 59, 48))
	b1t = Text(Point(75,75), "1")
	b1.draw(tablero)
	b1t.setFill("white")

	r2 = Rectangle(Point(110, 40), Point(180, 110))
	r2.setFill("black")
	r2.draw(tablero)
	r2.setOutline("black")
	r2t = Text(Point(145, 75), "2")
	r2t.setFill("white")

	b3 = Rectangle(Point(180, 40), Point(250, 110))
	b3.setFill(color_rgb(255, 59, 48))
	b3.draw(tablero)
	b3t = Text(Point(215, 75), "3")
	b3t.setFill("white")

	r4 = Rectangle(Point(40, 110), Point(110, 180))
	r4.setFill("black")
	r4.draw(tablero)
	r4t = Text(Point(75, 145), "4")
	r4t.setFill("white")
	
	b5 = Rectangle(Point(110,110), Point(180, 180))
	b5.setFill(color_rgb(255, 59, 48))
	b5.draw(tablero)
	b5t = Text(Point(145, 145), "5")
	b5t.setFill("white")

	r6 = Rectangle(Point(180, 110), Point(250, 180))
	r6.setFill("black")
	r6.draw(tablero)
	r6t = Text(Point(215, 145), "6")
	r6t.setFill("white")

	b7 = Rectangle(Point(40, 250), Point(110, 180))
	b7.setFill(color_rgb(255, 59, 48))
	b7.draw(tablero)
	b7t = Text(Point(75, 215), "7")
	b7t.setFill("white")


	r8 = Rectangle(Point(110, 180),Point(180, 250)) 
	r8.setFill("black")
	r8.draw(tablero)
	r8t = Text(Point(145, 215), "8")
	r8t.setFill("white")

	b9 = Rectangle(Point(180, 180), Point(250,250))
	b9.setFill(color_rgb(255, 59, 48))
	b9.draw(tablero)
	b9t = Text(Point(215, 215), "9")
	b9t.setFill("white")


	#Texto
	winner_string = Text(Point(130, 315), "")
	winner_string.setSize(20)
	winner_string.setFill("white")
	winner_string.draw(tablero)

	now = Text(Point(145, 280), "Usted puede ganar con: ")
	now.setSize(20)
	now.setFill(color_rgb(255, 59, 48))
	now.draw(tablero)

	b1t.draw(tablero)
	r2t.draw(tablero)
	b3t.draw(tablero)
	r4t.draw(tablero)
	b5t.draw(tablero)
	r6t.draw(tablero)
	b7t.draw(tablero)
	r8t.draw(tablero)
	b9t.draw(tablero)

	b1t.setSize(20)
	r2t.setSize(20)
	b3t.setSize(20)
	r4t.setSize(20)
	b5t.setSize(20)
	r6t.setSize(20)
	b7t.setSize(20)
	r8t.setSize(20)
	b9t.setSize(20)


	k = 0
	cond = False
	#Comenzando animacion
	for i in mostrar:

		winner_string.setFill("white")
		winner_string.setText(i)

		if(k > 3):
			break

		else:
			k+=1

		for j in i:

			if j == '1':
				b1t.setSize(30)
				b1t.setText("♗")
				time.sleep(0.8)
				b1t.setSize(18)
				b1t.setText("1")

			elif j == '2':
				r2t.setSize(30)
				r2t.setText("♗")
				time.sleep(0.8)
				r2t.setSize(18)
				r2t.setText("2")

			elif j == '3':
				b3t.setSize(30)
				b3t.setText("♗")
				time.sleep(0.8)
				b3t.setSize(18)
				b3t.setText("3")

			elif j == '4':
				r4t.setSize(30)
				r4t.setText("♗")
				time.sleep(0.8)
				r4t.setSize(18)
				r4t.setText("4")

			elif j == '5':
				b5t.setSize(30)
				b5t.setText("♗")
				time.sleep(0.8)
				b5t.setSize(18)
				b5t.setText("5")

			elif j == '6':
				r6t.setSize(30)
				r6t.setText("♗")
				time.sleep(0.8)
				r6t.setSize(18)
				r6t.setText("6")

			elif j == '7':
				b7t.setSize(30)
				b7t.setText("♗")
				time.sleep(0.8)
				b7t.setSize(18)
				b7t.setText("7")

			elif j == '8':
				r8t.setSize(30)
				r8t.setText("♗")
				time.sleep(0.8)
				r8t.setSize(18)
				r8t.setText("8")

			elif j == '9':
				b9t.setSize(30)
				b9t.setText("♗")
				time.sleep(0.8)
				b9t.setSize(18)
				b9t.setText("9")
		

	tablero.getMouse()
	tablero.close()





def evaluar_string(cadena):
	temporal = open("temporal.txt", "w+")
	combinaciones = open("combinaciones.txt", "r+")
	combinaciones_ganadoras = open("combinaciones_ganadoras.txt", "r+")
	anteriores = " "
	status = '1'
	ganadores = []
	err = False

	for k in cadena:

		anteriores = combinaciones.readline()

		while(anteriores != ""):
			anteriores = anteriores.rstrip('\n')
			status = anteriores[len(anteriores)-1]
			caminos = get_caminos(status, k)

			if(caminos[0] == '-1'):
				print("Cadena no valida \n\n")
				raw_input("")
				os.system('clear')
				err = True
				break;

			for j in caminos:
				temporal.write(anteriores + j + "\n")

			anteriores = combinaciones.readline()


		combinaciones.close()
		temporal.close()
		os.remove("combinaciones.txt")
		os.rename("temporal.txt", "combinaciones.txt")
		combinaciones = open("combinaciones.txt", "r+")
		temporal = open("temporal.txt", "w+")

	os.remove("temporal.txt")
	winner = combinaciones.readline()

	while(winner != ""):
		winner = winner.rstrip('\n')
		status = winner[len(winner)-1]

		if(status == '9'):
			ganadores.append(winner)

		winner = combinaciones.readline()

	j = 0;
	mostrar = []

	if ganadores != [] :

		for i in ganadores:
			combinaciones_ganadoras.write(i + "\n")

			if j<3:
				mostrar.append(i)
				j+=1
		combinaciones_ganadoras.close()
		tablero(mostrar)
	
	elif(err == False):		
		os.system('clear')
		combinaciones_ganadoras.write("No existen combinaciones ganadoras\n\n")
		raw_input("No existen combinaciones ganadoras")
		os.system('clear')


def main():

	os.system('clear')

	cond = True

	while cond:
		print("Que desea hacer?")
		print("1)Generar una cadena y evaluarla")
		print("2)Evaluar una cadena")
		print("3)Leer desde archivo")
		print("4)Salir")

		opc = raw_input("----->")

		if(opc == '1'):

			combinaciones = open("combinaciones.txt", "w+")
			combinaciones_ganadoras = open("combinaciones_ganadoras.txt", "w+")
			combinaciones.write("1\n")
			combinaciones.close()
			combinaciones_ganadoras.close()
			anteriores = " "
			cadena = generar_cadena()
			raw_input("La cadena generada es: " + cadena)

			evaluar_string(cadena)
			combinaciones.close()
			combinaciones_ganadoras.close()

		elif(opc == '2'):
			combinaciones = open("combinaciones.txt", "w+")
			combinaciones_ganadoras = open("combinaciones_ganadoras.txt", "w+")
			combinaciones.write("1\n")
			combinaciones.close()
			combinaciones_ganadoras.close()
			anteriores = " "
			cadena = raw_input("Ingresa una cadena: ")
			evaluar_string(cadena)
			combinaciones.close()
			combinaciones_ganadoras.close()



		elif opc == '3':

			file_name = raw_input("Ingresa el nombre del archivo con su extension: ")

			try:
				file = open(file_name, "r")
			except:
				print("Error al abrir el archivo")
				raw_input()
				os.system('clear')
				continue

			evaluar_string(file.readline())

		elif opc == '4':
			break;

		else:
			cadena = raw_input("Opción no valida, intente de nuevo")


		os.system('clear')


main()
