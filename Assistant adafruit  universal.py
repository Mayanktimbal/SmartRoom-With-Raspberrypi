

from Adafruit_IO import MQTTClient
import RPi.GPIO as GPIO
 
ADAFRUIT_IO_KEY      = '#ADD_YOUR_AIO_KEY'       
ADAFRUIT_IO_USERNAME = '#ADD_YOUR_USERNAME' 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) # light GPIO pin number
GPIO.setup(15,GPIO.OUT) # fan GPIO pin number
                                         
def connected(client):
  
    print ('Connected . Listening changes...')
 
    client.subscribe('FEED1')   #change to your feed1 name
    client.subscribe('FEED2')     #change to your feed2 name
 
def disconnected(client):
   
    print ('Disconnected from Adafruit IO!')
 
def message(client, feed_id, status):
   
    print('Feed {0} received new value: {1}'.format(feed_id, status))
 
    if feed_id == 'FEED1':     #change to your feed1 name
        if status=='ON' :
            print("Lights ON")  
            GPIO.output(18,GPIO.HIGH)
        else:
            print("Lights OFF")
            GPIO.output(18,GPIO.LOW)
    elif feed_id == 'FEED2':   #change to your feed2 name
          if status=='ON' :
            print("fan ON")
            GPIO.output(15,GPIO.HIGH)
          else:
            print("fan OFF")
    		GPIO.output(15,GPIO.LOW)
   
 
 
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
 
client.connect()

client.loop_blocking()