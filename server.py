"""Server itself."""
import json
import os
import socket

from get import get_weather_by_city

EXIT_MSG = os.environ.get('EXIT_MSG', default='q')
HOST = os.environ.get('HOST', default='127.0.0.1')
PORT = int(os.environ.get('PORT', default=8000))
server = socket.socket()

server.bind((HOST, PORT))

server.listen()

client, addr = server.accept()
while True:

    msg = client.recv(1024).decode()
    if msg == EXIT_MSG:
        break

    msg = msg.split()
    reply = get_weather_by_city((float(msg[0]), float(msg[1])))
    reply_string = json.dumps(reply)
    client.send((reply_string).encode())

client.close()
server.close()
