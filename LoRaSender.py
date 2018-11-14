from time import sleep
from ssd1306_i2c import Display
from machine import Pin
from dht import DHT11

def send(lora):
    d = DHT11(Pin(17))
    counter = 0
    
    display = Display()
    
    while True:
        d.measure()
        
        payload = 'Temp: {0} Hum: {1} '.format(d.temperature(), d.humidity())
        #print("Sending packet: \n{}\n".format(payload))
        display.show_text_wrap("Send {0} ".format(payload))
        lora.println(payload)

        counter += 1
        sleep(5)
