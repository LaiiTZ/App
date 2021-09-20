import time
from SensorDB import SensorBase

def on_message():
    topic = "asdasd"
    payload = "sss"
    print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" "+topic+" "+str(payload))
    sensor = SensorBase(topic,payload)
    sensor.guardar()
    sensor.mostrar()    

on_message()