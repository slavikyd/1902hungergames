"""Tests but it is client in disguise."""
import os
import socket

import correct

EXIT_MSG = os.environ.get('EXIT_MSG', default='q')
HOST = os.environ.get('HOST', default='127.0.0.1')
PORT = int(os.environ.get('PORT', default=8000))
client = socket.socket()

FIRST = '{"forecast": {"date": "2024-02-20", "date_ts": 1708376400, "week": 8, "sunrise": "07:12", "sunset": "17:55", "moon_code": 14, "moon_text": "moon-code-14", "parts": [{"part_name": "night", "temp_min": 6, "temp_avg": 7, "temp_max": 7, "temp_water": 10, "wind_speed": 3.1, "wind_gust": 4.1, "wind_dir": "n", "pressure_mm": 768, "pressure_pa": 1023, "humidity": 87, "prec_mm": 0.4, "prec_prob": 20, "prec_period": 480, "icon": "bkn_-ra_n", "condition": "light-rain", "feels_like": 4, "daytime": "n", "polar": false}, {"part_name": "morning", "temp_min": 6, "temp_avg": 8, "temp_max": 9, "temp_water": 10, "wind_speed": 3.6, "wind_gust": 5.2, "wind_dir": "e", "pressure_mm": 768, "pressure_pa": 1023, "humidity": 82, "prec_mm": 5.1, "prec_prob": 30, "prec_period": 360, "icon": "ovc_ra", "condition": "rain", "feels_like": 4, "daytime": "d", "polar": false}]}}'
SECOND = '{"forecast": {"date": "2024-02-20", "date_ts": 1708351200, "week": 8, "sunrise": "07:56", "sunset": "18:15", "moon_code": 14, "moon_text": "moon-code-14", "parts": [{"part_name": "morning", "temp_min": -22, "temp_avg": -21, "temp_max": -20, "wind_speed": 3.3, "wind_gust": 6.8, "wind_dir": "s", "pressure_mm": 759, "pressure_pa": 1011, "humidity": 78, "prec_mm": 0.6, "prec_prob": 40, "prec_period": 360, "icon": "ovc_-sn", "condition": "light-snow", "feels_like": -27, "daytime": "d", "polar": false}, {"part_name": "day", "temp_min": -19, "temp_avg": -18, "temp_max": -17, "wind_speed": 5.4, "wind_gust": 9.8, "wind_dir": "s", "pressure_mm": 760, "pressure_pa": 1012, "humidity": 68, "prec_mm": 0.3, "prec_prob": 30, "prec_period": 360, "icon": "bkn_-sn_d", "condition": "light-snow", "feels_like": -25, "daytime": "d", "polar": false}]}, "date": "2024-02-19T15:08:54.300797Z"}'
THIRD = '{"forecast": {"date": "2024-02-20", "date_ts": 1708376400, "week": 8, "sunrise": "06:41", "sunset": "17:26", "moon_code": 14, "moon_text": "moon-code-14", "parts": [{"part_name": "night", "temp_min": 3, "temp_avg": 4, "temp_max": 4, "temp_water": 6, "wind_speed": 3.6, "wind_gust": 7.6, "wind_dir": "nw", "pressure_mm": 771, "pressure_pa": 1027, "humidity": 92, "prec_mm": 1.8, "prec_prob": 40, "prec_period": 480, "icon": "ovc_-ra", "condition": "light-rain", "feels_like": 0, "daytime": "n", "polar": false}, {"part_name": "morning", "temp_min": 2, "temp_avg": 3, "temp_max": 3, "temp_water": 6, "wind_speed": 4.4, "wind_gust": 9.2, "wind_dir": "nw", "pressure_mm": 773, "pressure_pa": 1030, "humidity": 93, "prec_mm": 1, "prec_prob": 20, "prec_period": 360, "icon": "ovc_ra_sn", "condition": "wet-snow", "feels_like": -2, "daytime": "d", "polar": false}]}, "date": "2024-02-19T15:09:20.658587Z"}'


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

    msg = client.recv(2048).decode()
    print(f'Server response msg: {msg}')
    if city == 'Sirius' and msg == FIRST:
        print('Correct data recieved')
  

    elif city == 'Makhachkala' and msg == THIRD:
        print('Correct data recieved')

    elif city == 'Python' and msg == SECOND:
        print('Correct data recieved')
    else:
        print('WA')
        break
client.close()
