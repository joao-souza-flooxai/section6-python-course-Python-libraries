class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade) :
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return
        print(f'Voce comprou {quantidade} ingressos. 'f'Ainda temos {self.estoque}')
        self.estoque -= quantidade

if __name__ == '__main__': 
    ingressos = Ingressos(30)
    for i in range(1, 20):
        ingressos.comprar(i)