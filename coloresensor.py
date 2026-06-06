from pybricks.ev3devices import ColorSensor as coloresensor
from utility import convert_form_String_to_Port

class Farbsensor():
    def __init__(self, port):
        self.sensor = coloresensor(convert_form_String_to_Port(port))
    
    def farbe(self):
        return self.sensor.color()