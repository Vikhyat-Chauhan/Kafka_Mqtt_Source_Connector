from kafka import KafkaProducer
import paho.mqtt.client as paho
import yaml
import json  

#setting up Mqtt Server credentials(setup up a local mosquitto instance
broker = "0.0.0.0"
username = 'username'                                                      #Remove this Username if you dont have authentication (Not recommended)
password = 'password'                                                      #Remove this Password if you dont have authentication (Not recommended)
port = 1883

#setting up Kafka Server credentials
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#define mqtt callback
def on_message(client, userdata, message):
    print('Topic : '+ str(message.topic)),
    print('Payload : '+ str(message.payload.decode("utf-8")))
    print('                                    ')
    
    #Breaking down the topic(Example - devices/chipid/) into Kafka_topic, Chipid Key for kafka and the remaining topic and payload
    mqtt_topic = str(message.topic)                                        #Extract topic in String payload.
    mqtt_payload = str(message.payload.decode("utf-8"))                    #Extract payload in new String variable
    x = mqtt_topic.partition("/")                                          #Lets Split the topic in 3 parts
    kafka_topic = x[0]                                                     #Lets get the first object from the split i.e devices topic in this case
    mqtt_topic = x[2]                                                      #Put the remaining topic back into tha variable
    x = mqtt_topic.partition("/")                                          #Lets split the remaining topic again
    device_kafka_topic_chipid = x[0]                                       #Chip id generated that is to be used as key in kafka
    mqtt_topic = x[2]                                                      #remaining mqtt topic after removal of device/chipid/
    
    #Finally sending the Kafka Producer message
    producer.send(kafka_topic, key=device_kafka_topic_chipid, value=message.payload) #here we are keeping the key unique

    

client = paho.Client("server-001")         #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
#Bind function to callback
client.on_message=on_message
#Setup the Mqtt client 
client.username_pw_set(username,password)  #Remove this if there is no authentication(Not recommended)
client.connect(broker,port,60)
client.loop_start()                        #start loop to process received messages
print("Started MQTT Communication")

#Subscribe with the prescribed topics discribed in the .yaml file
with open(r'./producer_config.yaml') as file:                              #open the Yaml file, dont forget to place this inside the same folder as the script
    documents = yaml.load(file, Loader=yaml.FullLoader)                    #Load the Yaml file into the documents object
    mqtt_topics_allowed = documents[0]                                     #Now lets get the list from the first topic available(mqtt topics)                               
    for topic in mqtt_topics_allowed['mqtt_topics']:                       #Now lets parse through the mqtt topics in the list and subscribe to them
        print('Just Subscribed to ' + str(topic))   
        client.subscribe(str(topic)+'/#',0)                                #Subscribed to the particular topic
