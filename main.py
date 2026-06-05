#!/usr/bin/env pybricks-micropython
from pybricks.parameters import *
from motor import Motor
from button import Button
from utility import wait
from colores import *
from coloresensor import ColorSensor


motor = Motor("D", "A")
ColorSensor = ColorSensor("4")


while True:
    if ColorSensor.color() == blue:
        print("Hi")
    else:
        print(ColorSensor.color())