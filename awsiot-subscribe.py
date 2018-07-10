import paho.mqtt.client as mqtt
import ssl, random
from time import sleep

mqtt_url = "aum2n475z1n7e.iot.us-east-2.amazonaws.com"
root_ca = './certs/iotRootCA.pem'
public_crt = './certs/deviceCert.crt'
private_key = './certs/deviceCert.key'
mqtt_port = 8883

def on_connect(client, userdata, flags, response_code):
    print("Connected with status: {0}".format(response_code))
    client.subscribe("#", 1)

def on_message(client, userdata, msg):
    print "------ON MESSAGE!!!!"
    print(msg.topic + " -- " + str(msg.payload))

if __name__ == "__main__":
    print "Loaded MQTT configuration information."
    print "Endpoint URL: " + mqtt_url
    print "Root Cert: " + root_ca
    print "Device Cert: " + public_crt
    print "Private Key: " + private_key
    
    client = mqtt.Client()
    client.tls_set(root_ca, 
                   certfile = public_crt, 
                   keyfile = private_key, 
                   cert_reqs = ssl.CERT_REQUIRED, 
                   tls_version = ssl.PROTOCOL_TLSv1_2, 
                   ciphers = None)

    client.on_connect = on_connect
    client.on_message = on_message

    print "Connecting to AWS IoT Broker..."
    client.connect(mqtt_url, mqtt_port, keepalive=60)
    client.loop_forever()

