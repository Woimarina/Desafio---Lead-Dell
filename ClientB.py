import paho.mqtt.client as mqtt
import json
import os

def on_connect(client, userdata, flags, rc):
    print("Conectado. resulta: {}".format(str(rc)))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Mensagem recebida " + msg.topic + ": " + str(msg.payload))
    lido = json.loads(msg.payload)
    if lido['comando'] == 1:
        os.startfile("C:\Program Files (x86)\Windows NT\Accessories\wordpad.exe")
        print('comando recebido: {}'.format(lido['comando']))

    else:
        print('comando recebido: {}'.format(lido['comando']))

log = input(str("usuario: "))
pword = input(str("senha: "))
host = input(str("host: "))
topic = input(str("topico: "))

clientB = mqtt.Client("ClientB")
clientB.enable_logger()
clientB.username_pw_set(log, pword)
clientB.on_connect = on_connect
clientB.on_message = on_message
clientB.connect(host, 1883, 60)
clientB.loop_forever()