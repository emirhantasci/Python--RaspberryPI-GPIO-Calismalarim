from pirc522 import RFID
import signal
import time
import RPi.GPIO as GPIO
GPIO.setwarnings (False)

yesilled = 7
kirmiziled=13
sariled=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(yesilled, GPIO.OUT)
GPIO.setup(sariled, GPIO.OUT)
GPIO.setup(kirmiziled, GPIO.OUT)
oku = RFID()
util = oku.util()
util.debug = True
GPIO.output(yesilled, False)
while True:
    try:
        GPIO.output(sariled, True)
        oku.wait_for_tag()
        (error, data) = oku.request()
        if not error:
            print("\nKart Algilandi!")
            (error, kartid) = oku.anticoll()
            if not error:
                # Print UID
                kart = str(kartid[0])+" "+str(kartid[1])+" "+str(kartid[2])+" "+str(kartid[3])+" "+str(kartid[4])
                print(kart)
                kirmiziled=13
                sariled=11
                if kart == "138 147 109 21 97":
                    print("YEŞİL LED ON")
                    GPIO.output(yesilled, True)
                    GPIO.output(kirmiziled, False)
                    GPIO.output(sariled, False)
                else:
                    print("YEŞİL LED OFF")
                    GPIO.output(yesilled, False)
                    GPIO.output(kirmiziled, True)
                    time.sleep(0.5)
                    GPIO.output(kirmiziled, False)
                    time.sleep(0.5)
                    GPIO.output(kirmiziled, True)
                    time.sleep(0.5)
                    GPIO.output(kirmiziled, False)
                    time.sleep(0.5)
                    GPIO.output(kirmiziled, True)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break