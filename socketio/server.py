#servidor com socketio

import socketio

sio = socketio.Client() #criando um client servidor/standart python

@sio.event
def connect():
    print('conexão estabelecida')

@sio.event
def disconnect():
    print ('desconectado do servidor')

@sio.event
def my_message(data):
    print('mensagem recebida: {}'.format(data))
    sio.emit('my response', {'response': 'my response'})


sio.connect('http://localhost:5000')
sio.wait()

