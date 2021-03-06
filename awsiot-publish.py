import paho.mqtt.client as mqtt
import ssl, random
from time import sleep

mqtt_url = "aum2n475z1n7e.iot.us-east-2.amazonaws.com"
root_ca = './certs/iotRootCA.pem'
public_crt = './certs/devCert.pem'
private_key = './certs/devCert.key'

connflag = False

def on_connect(client, userdata, flags, response_code):
    global connflag 
    connflag = True   
    print("Connected with status: {0}".format(response_code))

def on_publish(client, userdata, mid):
    print userdata + " -- " + mid
    #client.disconnect()

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
#    client.on_publish = on_publish

    print "Connecting to AWS IoT Broker..."
    client.connect(mqtt_url, port = 8883, keepalive=60)
    client.loop_start()
#    client.loop_forever()

    while 1==1:
        sleep(0.5)
        print connflag
        if connflag == True:
            print "Publishing..."
            ap_measurement = random.uniform(25.0, 150.0)
            client.publish("ActivePower", ap_measurement, qos=1)
            print("ActivePower published: " + "%.2f" % ap_measurement )
        else:
            print("waiting for connection...")


