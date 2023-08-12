import wifimgr #Import the fuction created by us to autoconnect to a wifi
import time
from btcprice import get_btc_price
from machine import Pin, SoftI2C
import ssd1306
import stkprice
import ledblink


print('antes')
ledblink.led_reboot() #turn off all GPIOS that turn on/off leds
print('depois')

### PRE DEFINITIONS OF DISPLAY
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0) #First display cleaning after program start
### END OF PRE DEFINITIONS OF DISPLAY


wifimgr.connect() # Autoconnect to internet! To change SSID and PASSWORD, do it in wifimgr.py file.

i=0
while True :
    
    oled.fill(0) #Clear the script every step of loop
    
    #BITCOIN PRICE
    print(get_btc_price())
    oled.text('BITCOIN (USD)', 0, 0)
    oled.text(get_btc_price(), 0, 10)
    #END OF BITCOIN PRICE
    
    itsa = stkprice.itsa_difference()
    
    #ITSA3 PRICE
    print(itsa[0])
    oled.text(f'ITSA3 (R): {str(itsa[0])}', 0, 25)
    #END OF ITSA3 PRICE
    
    #ITSA4 PRICE
    print(itsa[1])
    oled.text(f'ITSA4 (G): {str(itsa[1])}', 0, 35)
    #END OF ITSA3 PRICE
    
    #DIFFERENCE BETWEEN ITSA
    print(itsa[1])
    oled.text(f'DELTA: {str(itsa[2])}%', 0, 45)
    oled.text(f'MEDIANA: {str(itsa[3])}%', 0, 55)
    #END OF DIFFERENCE BETWEEN ITSA
    
    oled.show() #show all data above
    stkprice.purchase_decision(itsa[2], itsa[3], itsa[4])
    print(f'Ciclo: {i}')
    time.sleep(5)
    i+=1



print('End Program')

