import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#setting up PINS
instance = dht11.DHT11(pin=14)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Main Program
while True:
    result = instance.read()
    soilValue = GPIO.input(15)
    datetimestamp =  str(datetime.datetime.now())
    temperature = 0
    humidity = 0
    if result.is_valid():
        temperature = result.temperature
        print("Temperature: %d C" % temperature)
        humidity = result.humidity
        print("Humidity: %d %%" % humidity)
        print("Soil Moisture: %d " % soilValue)
        URLTemperature = "http://192.168.225.107:8080/ashish/updateSensor?sid=1&email=amaurya080197@gmail.com&value="+str(temperature)
        r = requests.get(url = URLTemperature)
        URLHumidity = "http://192.168.225.107:8080/ashish/updateSensor?sid=3&email=amaurya080197@gmail.com&value="+str(humidity)
        r1 = requests.get(url = URLHumidity)
        URLsoil = "http://192.168.225.107:8080/ashish/updateSensor?sid=9&email=amaurya080197@gmail.com&value="+str(soilValue)
        r2 = requests.get(url = URLsoil)
        #print (r.text)
    time.sleep(2)