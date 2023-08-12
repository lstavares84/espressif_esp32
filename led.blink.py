#Tested on HiLetGo ESP32 WROOM Module


import machine #for Pin() function
import time #for sleep() function

rest_time=0.5 #time of blinking

led1 = machine.Pin(21, machine.Pin.OUT) #It was used GPIO 21 to run this test.

led1.off() #When the microcontroller is turned on or restarted, this guarantees that the LED will be in the initial operating stage.

while True:
  led1.on()
  time.sleep(rest_time)
  led1.off()
  time.sleep(rest_time)
