import argparse
import datetime
import re
import paho.mqtt.client as mqtt
import math

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
        
parser = argparse.ArgumentParser(description='efergyParser')
parser.add_argument('--url', required=True, type=str)
parser.add_argument('--dataFile', required=True, type=str)
parser.add_argument('--brokerUrl', required=True, type=str)
parser.add_argument('--brokerPort', required=True, type=str)
args = parser.parse_args()

baseUrl = args.url
dataFile = args.dataFile
brokerUrl = args.brokerUrl
brokerPort = args.brokerPort

mqttUserName = "your-broker-username-here"
mqttPassword = "your-broker-password-here"

f = open(dataFile, 'r')
client = mqtt.Client()  # create new instance
client.username_pw_set(mqttUserName, mqttPassword)

theIntPort = safe_cast(brokerPort, int)
client.connect(brokerUrl, theIntPort)    
        
for line in f:
    attributes = line.split(",")
    numberOfAttributes = len(attributes)
    if (numberOfAttributes == 3):
        myDateString = attributes[0]
        myDateString = myDateString.rstrip()
        myTimeString = attributes[1]
        myTimeString = myTimeString.rstrip()

        myDateString = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', myDateString)
        myTimeString = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', myTimeString)
        d = datetime.datetime.strptime(myDateString + "," + myTimeString, "%x,%H:%M:%S")
        theValueStr = str(attributes[2])
        theFloat = float(theValueStr)
        theFloat2 = theFloat / 1000    
        theValueStr2 = str(theFloat2)
        print("efergyParser: Publishing " + theValueStr2)
        client.publish("home/technical/power", theValueStr2, 0, True)
                
f.close()
