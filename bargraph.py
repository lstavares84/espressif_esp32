#Example of a 10 leds BarGraph (single color) tested on ESP32 HiLetGo WROOM

import machine #for Pin() function
import time #for sleep() function

rest_time=0.5 #set a default and standard blink time

#GPIO below were tested in a real circuit with a bargraph
led1 = machine.Pin(21, machine.Pin.OUT)
led2 = machine.Pin(19, machine.Pin.OUT)
led3 = machine.Pin(18, machine.Pin.OUT)
led4 = machine.Pin(5, machine.Pin.OUT)
led5 = machine.Pin(17, machine.Pin.OUT)
led6 = machine.Pin(16, machine.Pin.OUT)
led7 = machine.Pin(4, machine.Pin.OUT)
led8 = machine.Pin(0, machine.Pin.OUT)
led9 = machine.Pin(2, machine.Pin.OUT)
led10 = machine.Pin(15, machine.Pin.OUT)


def initial_stage(): #This function puts all leds of bargraph in the initial stage after microcontroller was restarted or turned on.
  led10.off()
  led9.off()
  led8.off()
  led7.off()
  led6.off()
  led5.off()
  led4.off()
  led3.off()
  led2.off()
  led1.off()

def turn_on(): #This function turn on all leds, one by one and keeps them on.
    led1.on()
    time.sleep(rest_time)
    led2.on()
    time.sleep(rest_time)
    led3.on()
    time.sleep(rest_time)
    led4.on()
    time.sleep(rest_time)
    led5.on()
    time.sleep(rest_time)
    led6.on()
    time.sleep(rest_time)
    led7.on()
    time.sleep(rest_time)
    led8.on()
    time.sleep(rest_time)
    led9.on()
    time.sleep(rest_time)
    led10.on()
    time.sleep(rest_time)
    
def turn_off(): #In this function, all leds will be turned off backwards of turn_on() function
    led10.off()
    time.sleep(rest_time)
    led9.off()
    time.sleep(rest_time)
    led8.off()
    time.sleep(rest_time)
    led7.off()
    time.sleep(rest_time)
    led6.off()
    time.sleep(rest_time)
    led5.off()
    time.sleep(rest_time)
    led4.off()
    time.sleep(rest_time)
    led3.off()
    time.sleep(rest_time)
    led2.off()
    time.sleep(rest_time)
    led1.off()
    time.sleep(rest_time)
    
# Below the "main" function.
while True:
  initial_stage()
  turn_on()
  turn_off()




