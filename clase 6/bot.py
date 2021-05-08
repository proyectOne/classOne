from threading import *
from datetime import datetime
import time
import requests
class Bot():
    def observadorReloj(self):
        while(True):
            time.sleep(0.2)
            now = datetime.now()
            horaactual=  now.strftime("%H:%M")
            print(horaactual)

            if(horaactual == '16:33'):
                self.saludarSuperheroe('batman')

    def saludarSuperheroe(self,nombre):
        url =str('http://localhost:4000/saludo/{}').format(nombre)
        r= requests.get(url)
        if r.status_code==200:
            print(r.text)


    def iniciar(self):
        t=Timer(1.0,self.observadorReloj)
        t.start()

def main():
    b = Bot()
    b.iniciar()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
    