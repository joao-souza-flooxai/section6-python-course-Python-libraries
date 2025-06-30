from time import sleep
from threading import Thread

class MeuThread (Thread) :
    def __init__(self, texto, tempo) :
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t = MeuThread('Thread 1', 5)
t.start()

t = MeuThread('Thread 2', 2)
t.start()


for i in range(20):
    print(i)
    sleep(1)