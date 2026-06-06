from pybricks.ev3devices import Motor as motorev3
import utility

class Motor():
    def __init__(self, motor_left_port, motor_right_port):
        self.motor_left = motorev3(utility.convert_form_String_to_Port(str(motor_left_port)))
        self.motor_right = motorev3(utility.convert_form_String_to_Port(str(motor_right_port)))
        self.speed = 200


    def vorwärts_fahren(self):
        self.motor_left.run(self.speed)
        self.motor_right.run(self.speed)
    

    def rückwärts_fahren(self):
        self.motor_left.run(-self.speed)
        self.motor_right.run(-self.speed)
    

    def links_drehen(self):
        self.motor_right.run_angle(self.speed, 166, wait=False)
        self.motor_left.run_angle(self.speed, -169)


    def rechts_drehen(self):
        self.motor_left.run_angle(self.speed, 150, wait=False)
        self.motor_right.run_angle(self.speed, -171)

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()

