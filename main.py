#!/usr/bin/env pybricks-micropython
from pybricks.parameters import *
from motor import Motor
from button import Button as Knopf
from utility import warte
from colores import *
from coloresensor import Farbsensor


motor = Motor("D", "A")

Sensor1 = Farbsensor("1")

while True:
    