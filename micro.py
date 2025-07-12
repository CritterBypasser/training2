#micropython code to blink an led at pin 26

import machine
led=machine.Pin(26, machine.Pin.OUT)
led.value(1)
