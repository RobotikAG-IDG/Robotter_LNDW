from pybricks.ev3devices import ColorSensor as coloresensor
from utility import convert_form_String_to_Port

class ColorSensor():
    def __init__(self, port):
        self.sensor = coloresensor(convert_form_String_to_Port(port))
    
    def color(self):
        return self.sensor.color()