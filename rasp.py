from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
import requests
import getpass


def get_user_id(login, password):
    payload = {'username': str(login), 'password': str(password)}
    host_backend = 'http://20.85.37.196:4000/login/'
    r = requests.post(host_backend, data=payload)
    if r.status_code == 200:
        return r.json()['id']
    else:
        raise Exception('Erro ao Obter ID por favor verifique as informações')


user = input('Digite seu login: ')
senha = getpass.getpass("Digite sua senha: ")

user_id = get_user_id(user, senha)


camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15

dataHora = datetime.now()
agora = dataHora.strftime('%d/%m/%Y %H:%M')

camera.start_preview()
camera.annotate_text = (agora)
camera.annotate_text_size = 70
sleep(5)
camera.capture('/Users/Juliana/Desktop/Upload.jpg')
camera.stop_preview()
