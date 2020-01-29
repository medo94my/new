from flask import Flask
import RPi.GPIO as GPIO
import time
import picamera
app=Flask(__name__)
counter =0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 27
GPIO.setup(LED,GPIO.OUT)
# GPIO.output(LED,GPIO.OUT)
# ledstats=GPIO.LOW
@app.route('/')
def index():

    return 'Welcom to the smart home System'


@app.route('/turn-on')
def onlight():
    GPIO.output(LED,GPIO.HIGH)
    return 'light on'
@app.route('/turn-off')
def offlight():
    off= GPIO.output(LED,GPIO.LOW)
    return 'lights off'
@app.route('/take-pic')
def pic():
    global counter
    path='/home/pi/new/flask-test/images/'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(path+"anny-{}.jpg".format(counter))
        counter+=1
    return'Picture Saved'



    return 'camera'
@app.route('/ac-on')
def ac_on():
    for count in range(2):
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(.5)
    return 'ac on'
@app.route('/ac-off')
def ac_off():
    for count in range(2):
        GPIO.output(LED,GPIO.LOW)
        time.sleep(2)
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(1)
    return 'ac-of'
if __name__ == '__main__':
    app.run(port=5000,debug=True)


