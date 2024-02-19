"""Tests but it is client in disguise."""
import os
import socket

import correct

EXIT_MSG = os.environ.get('EXIT_MSG', default='q')
HOST = os.environ.get('HOST', default='127.0.0.1')
PORT = int(os.environ.get('PORT', default=8000))
client = socket.socket()

client.connect((HOST, PORT))
cities = {
    'Sirius': (43.414115, 39.949259),
    'Makhachkala': (42.958372, 47.527544),
    'Python': (50.536936, 137.026989),
}
print(f'Bluetooth device connected succesfully. Exit message is {EXIT_MSG} btw')
while True:
    print(f'Use <{EXIT_MSG}> to quit.')
    city = input('Enter city name: ')
    if city == EXIT_MSG:
        print('Poka')
        break
    msg = cities[city]
    msg = [str(el) for el in msg]
    if msg == EXIT_MSG:
        break
    msg = ' '.join(msg)
    client.send(msg.encode())

    msg = client.recv(1024).decode()
    print(f'Server response msg: {msg}')
    if city == 'Sirius' and msg == correct.FIRST:
        print('Correct data recieved')
    else:
        print('WA')
        break

    if city == 'Makhachkala' and msg == correct.THIRD:
        print('Correct data recieved')
    else:
        print('WA')
        break
    if city == 'Python' and msg == correct.SECOND:
        print('Correct data recieved')
    else:
        print('WA')
        break
client.close()
