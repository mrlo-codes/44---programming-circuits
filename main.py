voltage = 0
test = 0
# This block sets the pin 0 to ON (1) to give power. To turn it off, set it to 0.
# 
# Note that the variables "test" and "voltage" had to be created in the Variables tab before using these blocks.
pins.digital_write_pin(DigitalPin.P0, 1)
# This block sets the value of the variable "test" to the value of the "voltage" read by the wire in pin 1. (From 0 to 1023, where 0 is no voltage to 1023, max voltage (around 3 V)).
# 
# The python code below prints out the value of test to the console. See the output by clicking on "Show data (Device)" on the left.

def on_forever():
    global test, voltage
    test = pins.analog_read_pin(AnalogPin.P1)
    voltage = (1024 - test) / 1024 * 3.3
    print("Analog read in: " + ("" + ("" + ("" + str(test)))) + " Voltage: " + ("" + ("" + ("" + str(voltage)))) + "V")
    if voltage >= 3:
        basic.show_string("L")
    elif voltage >= 1:
        basic.show_string("L")
    else:
        basic.show_number(0)
basic.forever(on_forever)
