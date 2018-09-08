#!/usr/bin/env python
# -*- coding: UTF-8-*-
import turtle
from turtle import *
title("ejer1")
penup()
goto(-60,-190)
turtle.backward
#setup(640,480,0,0)
def cuadrado():
	g=1
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(180)	
	pendown()
	while (g<=4):
		turtle.forward(50)
		turtle.left(90)
		g=g+1
	penup()
A=0
while (A<4):
		cuadrado()
		A=A+1
wait = input("PREsione enter.")
