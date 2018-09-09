#!/usr/bin/env python
# -*- coding: UTF-8-*-
import turtle
from turtle import *
title("ejer4")
penup()
goto(-300,-200)
x=int(input('Escriba el numero de lados del poligono a dibujar:'))
y=int(input('Escriba el numero de pisos de la piramide:'))
def poligono():
	g=0
	pendown()
	while (g<x):
		turtle.forward(200/x)
		turtle.left(180-(180/x)*(x-2))
		g=g+1
	penup()
	turtle.forward(600/x)
A=0
B=0
while A<y:
	B=A
	while B<y:
	  poligono()
	  B=B+1
	A=A+1
	goto(-300+(300/x)*A,-200+80*A)
wait = input("PREsione enter.")
