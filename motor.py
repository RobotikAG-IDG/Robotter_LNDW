from pybricks.ev3devices import Motor as motorev3
import utility

class Motor():
    def __init__(self, motor_left_port, motor_right_port):
        self.motor_left = motorev3(utility.convert_form_String_to_Port(str(motor_left_port)))
        self.motor_right = motorev3(utility.convert_form_String_to_Port(str(motor_right_port)))


    def move_forward(self, speed):
        self.motor_left.run(speed)
        self.motor_right.run(speed)
    

    def move_backward(self, speed):
        self.motor_left.run(-speed)
        self.motor_right.run(-speed)
    

    def turn_left(self, speed):
        self.motor_right.run_angle(speed, 166, wait=False)
        self.motor_left.run_angle(speed, -169)


    def turn_right(self, speed):
        self.motor_left.run_angle(speed, 150, wait=False)
        self.motor_right.run_angle(speed, -171)

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()

