#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import TouchSensor as button
from utility import convert_form_String_to_Port

class Button():
    def __init__(self, port):
        self.button = button(convert_form_String_to_Port(port))
    
    def is_pressed(self):
        return not self.button.pressed()
