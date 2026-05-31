from pybricks.parameters import Port


def convert_form_String_to_Port(port_string):
        if (port_string == "A"):
            return Port.A
        elif (port_string == "B"):
            return Port.B
        elif (port_string == "C"):
            return Port.C
        elif (port_string == "D"):
            return Port.D
        elif (port_string == "1"):
            return Port.S1
        elif (port_string == "2"):
            return Port.S2
        elif (port_string == "3"):
            return Port.S3
        elif (port_string == "4"):
            return Port.S4

def wait(time):
    from time import sleep
    sleep(time)