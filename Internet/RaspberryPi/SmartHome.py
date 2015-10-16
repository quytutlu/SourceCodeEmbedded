import serial,urllib,json
import urllib,json
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins=[5,6,13,19,16,26,20,21]
ID="5"
def Init():
        for i in range(0,8):
            GPIO.setup(Pins[i],GPIO.OUT)    
def KetNoiServer(url):
        JSON=urllib.urlopen(url)
        data = json.loads(JSON.read())
        #print len(data['data'])
        n=len(data['data'])
        i=0
        while (i < n):
                #print 'vi tri',i/4,':',data['data'][i+3:i+4]
                tt=0
                if data['data'][i+3:i+4]=='0':
                        tt=1
                GPIO.output(Pins[i/4],tt)
                i=i+4
Init()
while True:
        try:
            KetNoiServer('http://smarthometl.com/index.php?cmd=laytrangthaipi&id='+ID)
        except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit()