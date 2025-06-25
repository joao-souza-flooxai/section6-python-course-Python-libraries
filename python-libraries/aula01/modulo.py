def soma(a:float , b:float)->float:
    return a+b

def main():
    print(soma(10, 20))
    print(soma(20, 20))

#Permite executar testes em modulos, pois os prints só serão exibidos se o modulo for 
# executado diretamente(ele for o main) e não importado em outro lugar.
if __name__ == '__main__':
    main()
