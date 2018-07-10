require 'rubygems'
require 'mqtt'

mqtt_url = "aum2n475z1n7e.iot.us-east-2.amazonaws.com"
root_ca = './certs/iotRootCA.pem'
public_crt = './certs/deviceCert.crt'
private_key = './certs/deviceCert.key'

puts "Loaded MQTT configuration information."
puts "Endpoint URL: #{mqtt_url}"
puts "Root Cert: #{root_ca}"
puts "Device Cert: #{public_crt}"
puts "Private Key: #{private_key}\n\n"

puts "Connecting to AWS IoT Broker..."

client = MQTT::Client.connect(
      client_id: 'ruby-mqtt',
      host: mqtt_url,
      port: 8883,
      ssl: :TLSv1_2,
      cert_file: public_crt,
      key_file: private_key,
      ca_file: root_ca
)

if client.connected?
      puts "Successfully connected! exiting."
      client.disconnect()
      exit
else
      abort("Error connecting to AWS IoT, exiting.")
end


