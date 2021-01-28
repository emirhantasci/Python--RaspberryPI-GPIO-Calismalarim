import RPi.GPIO as GPIO # GPIO kutuphanesi scripte dahil edilmistir.
import time # time kutuphanesi scripte dahil edilmistir.

btnarti=14
btneksi=15
btnorta=18
servo = 17
deger=2.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(btnarti, GPIO.IN, pull_up_down=GPIO.PUD_UP) # btnarti pini giris olarak atanıp dahili olarak pull up direnc atanmistir.
GPIO.setup(btneksi, GPIO.IN, pull_up_down=GPIO.PUD_UP) # btneksi pini giris olarak atanıp dahili olarak pull up direnc atanmistir.
GPIO.setup(btnorta, GPIO.IN, pull_up_down=GPIO.PUD_UP) # btnorta pini giris olarak atanıp dahili olarak pull up direnc atanmistir.
p = GPIO.PWM(servo, 50) # servo pinin bagli oldugu cikis 50Hz bir frekans ile tetiklenmistir.
p.start(deger) # servo sinyalimiz 2.5 deger ile baslatılmıstır.
try:
  while True:
    artideger=GPIO.input(btnarti) # giris pininden gelen deger artideger degiskenine atanmistir.
    eksideger=GPIO.input(btneksi) # giris pininden gelen deger eksideger degiskenine atanmistir.
    ortadeger=GPIO.input(btnorta) # giris pininden gelen deger ortadeger degiskenine atanmistir.
    if artideger==False:
        deger+=0.2
        time.sleep(0.3)
    elif eksideger ==False:
        deger-=0.2
        time.sleep(0.3)
    elif ortadeger == False:
        deger=7.7
    if deger>12.5:
        deger=12.5
    elif deger<2.5:
        deger=2.5
    p.ChangeDutyCycle(deger)
    print(deger)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
