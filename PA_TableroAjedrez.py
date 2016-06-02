import turtle
import os

wind = turtle.Screen()
wind.bgcolor('lightblue')
wind.title('Tablero ajedrez')

tab=turtle.Turtle()
tab.speed(0)

def cuadrado(tam,var,color):
	tab.color(color)
	tab.begin_fill()
	for i in range(4):
		tab.fd(tam)
		tab.lt(90)
	tab.end_fill()
	tab.fd(tam)

def fila(tam,var,color1,color2):
	for i in range(4):
		if(var==True):
			cuadrado(tam,var,color1)
			cuadrado(tam,var,color2)
		else:
			cuadrado(tam,var,color2)
			cuadrado(tam,var,color1)

def tablero(tam,var,color1,color2):
	tab.pu()
	tab.goto(-(tam*4),(tam*4))