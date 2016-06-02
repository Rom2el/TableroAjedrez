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