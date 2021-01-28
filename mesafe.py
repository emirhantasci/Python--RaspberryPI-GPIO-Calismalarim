import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG_Pin = 23
ECHO_Pin = 24



GPIO.setup(TRIG_Pin,GPIO.OUT)
GPIO.setup(ECHO_Pin,GPIO.IN)

while True:

    GPIO.output(TRIG_Pin, False)
    time.sleep(2)

    GPIO.output(TRIG_Pin, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_Pin, False)

    while GPIO.input(ECHO_Pin)==0:
        ilk_darbe_sinyali = time.time()

    while GPIO.input(ECHO_Pin)==1:
        son_darbe_sinyali = time.time()

    fark = son_darbe_sinyali - ilk_darbe_sinyali

    mesafe = fark * 17150
    mesafe = round(mesafe, 2)

    if mesafe > 2 and mesafe < 400:
        print ("Olculen Mesafe:",mesafe - 0.5,"cm")
    else:
        print ("Olculemedi !!!")