import urequests
import json
import buzzer
import ledblink

def itsa_difference():
    
    median=2.36
    mode=0.7
    
    
    # Get, parse and isolate price of ordinary stock
    itsa3_get_data = urequests.get("https://mfinance.com.br/api/v1/stocks/ITSA3")
    itsa3_parsed_data = itsa3_get_data.json()
    itsa3_last_price = itsa3_parsed_data["lastPrice"]
    # END of get, parse and isolate price of ordinary stock
    
    # Get, parse and isolate price of preferential stock 
    itsa4_get_data = urequests.get("https://mfinance.com.br/api/v1/stocks/ITSA4")
    itsa4_parsed_data = itsa4_get_data.json()
    itsa4_last_price = itsa4_parsed_data["lastPrice"]
    # End of get, parse and isolate price of preferential stock 
    
    # Calculate the difference (%) between them. Always ordinary over preferential
    difference = round((((itsa3_last_price/itsa4_last_price)-1)*100),2)
    leds_difference = int(difference)
    # END OF Calculate the difference (%) between them. Always ordinary over preferential
    
    # Return Values
    return itsa3_last_price, itsa4_last_price, difference, median, mode
    
    
def purchase_decision(difference, median, mode):
    if difference >= median:
        print('Compre ITSA4 ou Swing ITSA3 -> ITSA4. Led Verde')
        ledblink.green_led.on()
        ledblink.yellow_led.off()
        ledblink.red_led.off()
    elif difference <= mode:
        print('Compre ITSA3 ou Swing ITSA4 -> ITSA3. Led Amarelo')
        ledblink.green_led.off()
        ledblink.yellow_led.on()
        ledblink.red_led.off()
    elif difference<=0:
        print('Acionar Buzzer (return buzzer) + LED VERMELHO PISCANTE')
        ledblink.green_led.off()
        ledblink.yellow_led.off()
        ledblink.red_led.on()
    else:
        print('Leds Desligados')