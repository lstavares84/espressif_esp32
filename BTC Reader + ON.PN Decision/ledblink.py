import machine #for Pin() function
import time #for sleep() function

rest_time=0.5 #time of blinking
red_led = machine.Pin(0, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)
green_led = machine.Pin(2, machine.Pin.OUT)
 
def led_reboot():
    red_led.off()
    yellow_led.off()
    green_led.off()
    
    i=0
    while i<2:
        red_led.on()
        time.sleep(1)
        yellow_led.on()
        time.sleep(1)
        green_led.on()
        time.sleep(1)
        green_led.off()
        time.sleep(1)
        yellow_led.off()
        time.sleep(1)
        red_led.off()
        time.sleep(1)
        i = i + 1
  
