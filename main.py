#!/usr/bin/env pybricks-micropython

from motor import Motor
from utility import wait


motor = Motor("D", "A")

def roboter_loop():
    motor.move_forward(500)
    wait(2)
    motor.move_backward(500)
    wait(2)
    motor.turn_left(500)
    motor.turn_right(500)


while True:
    roboter_loop()