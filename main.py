pins.digital_write_pin(DigitalPin.P0, 1)
test = 0

def on_forever():
    global test
    test = pins.analog_read_pin(AnalogPin.P0)
basic.forever(on_forever)
