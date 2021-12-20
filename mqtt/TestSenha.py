import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("testa conexão. resposta: {}".format(str(rc)))
    client.subscribe("marina", 1)

def on_message(client, userdata, msg):
    print("Mensagem recebida de: "+ msg.topic + "  " +str(msg.payload))


client = mqtt.Client("ClientC")
client.enable_logger()
client.username_pw_set("admin", "mq@IoT2019")
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.7", 1883, 60)
client.loop_forever()
