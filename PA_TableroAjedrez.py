#Importamos las librerias necesarias
import turtle



#asignamos las caracteristicas la ventana que mostrara el tablero
wind = turtle.Screen()
wind.bgcolor('lightblue')
wind.title('Tablero ajedrez')

tab=turtle.Turtle()
tab.speed(0)

#dibujamos el cuadro
def cuadrado(tam,var,color):
	tab.color(color)
	tab.begin_fill()
	for i in range(4):
		tab.fd(tam)
		tab.lt(90)
	tab.end_fill()
	tab.fd(tam)

#dibujamos las filas
def fila(tam,var,color1,color2):
	for i in range(4):
		if(var==True):
			cuadrado(tam,var,color1)
			cuadrado(tam,var,color2)
		else:
			cuadrado(tam,var,color2)
			cuadrado(tam,var,color1)

#dibujamos tablero
def tablero(tam,var,color1,color2):
	tab.pu()
	tab.goto(-(tam*4),(tam*4))
	for i in range(8):
		fila(tam,var,color1,color2)
		tab.bk(tam*8)
		tab.rt(90)
		tab.fd(tam)
		tab.lt(90)
		if(var==True):
			var=False
		else:
			var=True
	turtle.mainloop()

tablero(50,True,'black','white')