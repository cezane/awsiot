import paho.mqtt.client as mqtt
import ssl

mqtt_url = "aum2n475z1n7e.iot.us-east-2.amazonaws.com"
root_ca = './certs/iotRootCA.pem'
public_crt = './certs/deviceCert.crt'
private_key = './certs/deviceCert.key'

def on_connect(client, userdata, flags, response_code):
    print "OPAAAAAAAAA"
    print("Status: {0}".format(response_code))

def on_publish(client, userdata, mid):
    client.disconnect()

def on_message(client, userdata, msg):
    print "EPAAAAAA"
    print(msg.topic + " " + str(msg.payload))

if __name__ == "__main__":
    print "Loaded MQTT configuration information."
    print "Endpoint URL: " + mqtt_url
    print "Root Cert: " + root_ca
    print "Device Cert: " + public_crt
    print "Private Key: " + private_key
    
    client =mqtt.Client("aws_connector")
    client.tls_set(root_ca, 
                   certfile = public_crt, 
                   keyfile = private_key, 
                   cert_reqs = ssl.CERT_REQUIRED, 
                   tls_version = ssl.PROTOCOL_TLSv1_2, 
                   ciphers = None)

    client.on_connect = on_connect
    client.on_message = on_message

    print "Connecting to AWS IoT Broker..."
    client.connect(mqtt_url, port = 8883)
    

#client = MQTT::Client.connect(
#      client_id: 'ruby-mqtt',
#      host: mqtt_url,
#      port: 8883,
#      ssl: :TLSv1_2,
#      cert_file: public_crt,
#      key_file: private_key,
#      ca_file: root_ca
#)

#if client.connected?
#      print "Successfully connected! exiting."
#      client.disconnect()
#      exit
#else
#      abort("Error connecting to AWS IoT, exiting.")
#end


