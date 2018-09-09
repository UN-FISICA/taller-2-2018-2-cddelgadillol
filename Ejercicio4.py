#!/usr/bin/env python
# -*- coding: UTF-8-*-
import turtle
from turtle import *
title("ejer3")
penup()
goto(-200,-200)
x=int(input('Escriba el numero de lados del poligono a dibujar:'))
y=int(input('Escriba el numero de lados del poligono invisible:'))
def poligono(tamaño,lados,tipo,inicio,lados2):
	g=0
	turtle.left(360-(360/(lados2))*inicio)
	while (g<lados):
		turtle.forward(tamaño/lados)
		if tipo>0:
		 turtle.left(360/lados)
		if tipo<1:
			pendown()
			poligono(100,x,1,g,lados)
			tipo=0
			g=g+1
			turtle.left((360/(lados))*g)
		else:
			g=g+1
		
	penup()
poligono(800,y,0,0,1)
wait = input("PREsione enter.")
