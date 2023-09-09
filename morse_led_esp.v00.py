#%serialconnect to --port=/dev/ttyUSB1 --baud=115200

from machine import Pin # para usar o pino/
from time import sleep # vai funcionar com um delay--baud=115200

led1red = Pin(0, Pin.OUT)
led2red = Pin(25, Pin.OUT)
led3red = Pin(19, Pin.OUT)
led4red = Pin(14, Pin.OUT)
led5red = Pin(17, Pin.OUT)

led1green = Pin(2, Pin.OUT)
led2green = Pin(26, Pin.OUT)
led3green = Pin(18, Pin.OUT)
led4green = Pin(12, Pin.OUT)
led5green = Pin(16, Pin.OUT)

led1blue = Pin(15, Pin.OUT)
led2blue = Pin(27, Pin.OUT)
led3blue = Pin(5, Pin.OUT)
led4blue = Pin(13, Pin.OUT)
led5blue = Pin(4, Pin.OUT)

ledred = [led1red, led2red, led3red, led4red, led5red]
ledgreen = [led1green, led2green, led3green, led4green, led5green]
ledblue = [led1blue, led2blue, led3blue, led4blue, led5blue]

def reset():
    led1red.off()
    led2red.off()
    led3red.off()
    led4red.off()
    led5red.off()

    led1green.off()
    led2green.off()
    led3green.off()
    led4green.off()
    led5green.off()

    led1blue.off()
    led2blue.off()
    led3blue.off()
    led4blue.off()
    led5blue.off()

def start():
    led1blue.on()
    sleep(0.25)
    led1blue.off()
    led2blue.on()
    sleep(0.25)
    led2blue.off()
    led3blue.on()
    sleep(0.25)
    led3blue.off()
    led4blue.on()
    sleep(0.25)
    led4blue.off()
    led5blue.on()
    sleep(0.25)
    led5blue.off()
    sleep(3)

def end():
    led5blue.on()
    sleep(0.25)
    led5blue.off()
    led4blue.on()
    sleep(0.25)
    led4blue.off()
    led3blue.on()
    sleep(0.25)
    led3blue.off()
    led2blue.on()
    sleep(0.25)
    led2blue.off()
    led1blue.on()
    sleep(0.25)
    led1blue.off()
    sleep(3)
        


international_morse = { 'A':'.-', 'B':'-...',
               'C':'-.-.', 'D':'-..', 'E':'.',
               'F':'..-.', 'G':'--.', 'H':'....',
               'I':'..', 'J':'.---', 'K':'-.-',
               'L':'.-..', 'M':'--', 'N':'-.',
               'O':'---', 'P':'.--.', 'Q':'--.-',
               'R':'.-.', 'S':'...', 'T':'-',
               'U':'..-', 'V':'...-', 'W':'.--',
               'X':'-..-', 'Y':'-.--', 'Z':'--..',
               '1':'.----', '2':'..---', '3':'...--',
               '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.',
               '0':'-----', ' ': ' '}


def morse(sentence):

### ENCONDING
    sentence_in_morse=''
    for letter in sentence:
 #       if letter == ' ':
 #           sentence_in_morse += ' '
 #       else:
            #sentence_in_morse += international_morse[letter.upper()] + ' ' #convert all sentence to morse it
            sentence_in_morse = international_morse[letter.upper()] #convert letter by letter do led matrix
            #print(sentence_in_morse)
            to_leds(sentence_in_morse)
    return sentence_in_morse
### END OF ENCONDING


#def to_leds(letters):
#    for symbol in range(5):
#        if letters[symbol] == ".":
#            ledred[symbol].on()
#            print('R')
#        elif letters[symbol] == "-":
#            ledgreen[symbol].on()
#            print('G')
#    sleep(3)
#    ledred[symbol].off()
#    ledgreen[symbol].off()
#    ledblue[symbol].off()
#    sleep(1)




def to_leds(sentence_in_morse):
    i=0
    reset()
    for letter in sentence_in_morse:
        if letter == ".":
            ledred[i].on()
            #print('R')
        elif letter == '-':
            ledgreen[i].on()
            #print('G')
        elif letter == " ":
            ledred[i].off()
            ledgreen[i].off()
            ledblue[i].off()
            #print('BBBBB')
        i = i+1
    sleep(5)
    reset()
    sleep(0.5)


while True:
    reset()   
    start()
    sentence='0 Amor Lindo 5'    
    sentence_encoded=morse(sentence) #in morse() the function to blink leds will be called
    end()




