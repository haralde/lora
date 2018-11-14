from ssd1306_i2c import Display

def receive(lora):
    print("LoRa Receiver")
    display = Display()

    while True:
        if lora.receivedPacket():
            lora.blink_led()

            try:
                payload = lora.read_payload()
                rssi = "RSSI: {0}".format(lora.packetRssi())
                snr = "SNR : {0}".format(lora.packetSnr())
                display.show_text_wrap("{0}".format(payload.decode()))
                display.show_text(rssi,0,20, False)
                display.show_text(snr,0,30, False)
                #print("*** Received message ***\n{}".format(payload.decode()))

            except Exception as e:
                print(e)
            #display.show_text("RSSI: {}\n".format(lora.packetRssi()), 10, 10)
            #print("with RSSI: {}\n".format(lora.packetRssi))
