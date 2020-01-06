

from Adafruit_IO import MQTTClient

 
ADAFRUIT_IO_KEY      = '#ADD_YOUR_AIO_KEY'       
ADAFRUIT_IO_USERNAME = '#ADD_YOUR_USERNAME' 
    
                                         
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
        else:
            print("Lights OFF")

    elif feed_id == 'FEED2':   #change to your feed2 name
          if status=='ON' :
            print("fan ON")
          else:
            print("fan OFF")
    
      ##  requests.post('{0}/widgets/temp'.format(DASHBOARD_URL), data={'value': payload})
 
 
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
 
client.connect()

client.loop_blocking()