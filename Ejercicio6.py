#!/usr/bin/env python
# -*- coding: UTF-8-*-
import turtle
from turtle import *
title("ejer4")
penup()
goto(-300,-200)
y=int(input('Escriba el numero de pisos de la piramide:'))
def poligono():
	g=0
	pendown()
	while (g<C):
		turtle.forward(200/C)
		turtle.left(180-(180/C)*(C-2))
		g=g+1
	penup()
	turtle.forward(70)
A=0
B=0
C=0
while A<y:
	B=A
	C=2+y-A
	while B<y:
	  poligono()
	  B=B+1
	A=A+1
	goto(-300+(35)*A,-200+70*A)
wait = input("PREsione enter.")
