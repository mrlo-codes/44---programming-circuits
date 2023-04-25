// This block sets the pin 0 to ON (1) to give power. To turn it off, set it to 0.
pins.digitalWritePin(DigitalPin.P0, 1)
// Note that the variable "test" had to be created in the Variables tab before using these blocks.
let test = 0
basic.forever(function () {
    // This block sets the value of the variable "test" to the value of the "voltage" read by the wire in pin 1. (From 0 to 1023, where 0 is no voltage to 1023, max voltage (around 3 V)).
    // 
    // The python code below prints out the value of test to the console. See the output by clicking on "Show data (Device)" on the left.
    test = pins.analogReadPin(AnalogPin.P1)
    console.log(test)
if (test >= 500) {
        basic.showString("H")
    } else if (test >= 300) {
        basic.showString("L")
    } else {
        basic.showNumber(0)
    }
})
