import LoRaDuplexCallback
#import LoRaPingPong
#import LoRaSender
import LoRaReceiver
import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller
from machine import Pin, SPI, UART, ADC
from ublox_gps import MicropyGPS
import time, utime


from ssd1306_i2c import Display




controller = ESP32Controller()
lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss = ESP32Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = ESP32Controller.PIN_ID_FOR_LORA_DIO0)

print("start")

#LoRaDuplexCallback.duplexCallback(lora)
#LoRaPingPong.ping_pong(lora)
#LoRaSender.send(lora)
#LoRaReceiver.receive(lora)


#gps test

# GPS initialization
uart = UART(1, 9600)                          # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1)  # init with given parameters

my_gps = MicropyGPS()

# DISPLAY initialization
display = Display()


display.show_text_wrap("Hallo")


while True:        
    try:
        pycom.rgbled(0x000500)  # hearbeat
        
        # Updating GPS position
        if(utime.ticks_ms() - updateGPS >= UPDATE_GPS):
            updateGPS = utime.ticks_ms()
            stat = my_gps.updateall(uart.readall())            
                
        # Reporting GPS Status
        if(stat != None):
            display.show_text("GPS status",0,20, False)
        else:
            display.show_text("No gps",0,30, False)    
        
      
                        
        # hearbeat
        time.sleep_ms(1000)
        # pycom.rgbled(0x050505)         
        time.sleep_ms(1000)                            
        
    except:     # gps problems
        # pycom.rgbled(0x220000) 
        display.show_text("GPS problems",0,30, False)     
        my_gps.stringclean()        
        time.sleep_ms(2000)    