# Kafka_Mqtt_Source_Connector
A Python 2.7 based Mqtt Source Connector script for Kafka..
![](pictures/Apache_Kafka_Connect_MQTT_Broker_Mosquitto_Integration.png)

## Steps 1 : Install Brew

                /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

## Steps 2 : Install & Run Mosquittto

   To test this service, lets install and run a mosquitto Mqtt server locally.
                
                brew install mosquitto
                
   On successfully installing, Lets run mosquitto Mqtt server locally.
      
                brew services start mosquitto

## Steps 3 : Installing Confluent Kafka in your PC 
  
  [I have already made a git repo, it will help you to run a local kafka service on your mac.](https://github.com/Vikhyat-Chauhan/Confluent-Kafka-Installing-on-MAC) 
 
## Step 4 : Now simply cd to the directory of the extracted zip source file and run the connector scripy
                
                cd Kafka_Mqtt_Source_Connector
                
                sudo python producer.py
   Note : Do check the dependancies in the python script and use pip install to get them.
   
#Link to some Resources that I found helpful.
  
  [Installing Confluent Kafka on your MAC](https://github.com/Vikhyat-Chauhan/Confluent-Kafka-Installing-on-MAC) 

  [Official Confluent Installation Guide](https://docs.confluent.io/5.4.2/cli/installing.html)
  
  [Installing Java8 on Mac - stackoverflow](https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac)
  
  [homebrew-cask-option-not-recognized - stackoverflow](https://stackoverflow.com/questions/30413621/homebrew-cask-option-not-recognized)
  
  [Youtube Video Guide on Setting up Confluent Installation](https://www.youtube.com/watch?v=5x5GnBhyTMI)
