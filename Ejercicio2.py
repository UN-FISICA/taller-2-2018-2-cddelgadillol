#!/usr/bin/env python
# -*- coding: UTF-8-*-
import turtle
from turtle import *
title("ejer2")
penup()
goto(-200,-200)
turtle.backward
#setup(640,480,0,0)
x=int(input('Escriba el numero de lados del poligono a dibujar:'))
def punt(l):
	if A>0:
	 turtle.left(90*A)
	turtle.forward(300)
	turtle.left(360-90*A)
def poligono():
	g=0
	pendown()
	while (g<x):
		turtle.forward(400/x)
		turtle.left(180-(180/x)*(x-2))
		g=g+1
	penup()
	punt(A)
A=0
while (A<4):
		poligono()
		A=A+1
wait = input("PREsione enter.")
