import paho.mqtt.client as mqtt
import random
import json

user = 'mqtt-test'
pword = 'mqtt-test'
host = 'localhost'
topic = 'teste'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('conectado. recebe: {}'.format(rc))
    else:
        print('falha ao conectar. retorna: {}'.format(rc))


def publish(client):
    i = 0
    while i<=10:
        msg = random.randint(0,5)
        payload = json.dumps({'comando': msg})
        print(payload)
        client.publish(topic, payload)
        i = i+1



client = mqtt.Client("Client")
client.enable_logger()
client.username_pw_set(user, pword)
client.connect(host, 1883, 60)
client.on_connect = on_connect
publish(client)
client.loop_start()
