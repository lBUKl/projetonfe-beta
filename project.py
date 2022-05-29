import time


def entrada():
    try:
        print('==' * 50)
        print('||  Olá, bem vindo ao script de cálculos.                                                         ||')
        print('||  Ao digitar porcentagens digite o numero inteiro (Ex 40,50).                                   ||')
        print('||  Ao digitar numeros decimais, pode utilizar tanto ponto como virgula.                          ||')
        print('||  Caso queira reiniciar os calculos, basta digitar qualquer letra ou palavra.                   ||')
        print('||  Ao calcular ICMS manualmente favor digitar o valor total dos produtos nos 2 primeiros campos. ||')
        print('||  Faça bom proveito.                                                                            ||')
        print('==' * 50)
        time.sleep(2)
        vt = float(input('Digite o valor total da Nota Fiscal:   ').replace(',', '.'))
        vp = float(input('Digite o valor dos produtos da Nota Fiscal:  ').replace(',', '.'))
        frete = float(input('Digite o valor do frete:   ').replace(',', '.'))
        vt2 = frete + vt
        dif = (vt2 - vp) / vp
        margem = float(input('Digite a porcentagem da margem de lucro:   ').replace(',', '.')) / 100
        imposto = float(input('Digite o valor fixo em % de imposto que será aplicado a todos os produtos:  ').replace(',', '.')) / 100
        resposta = (input('Deseja calcular o ICMS manualmente para cada produto ? (S/N) '))
        while True:
            if resposta in ['S', 's']:
                while True:
                    ipi = float(input('Digite o ICMS do produto:  ').replace(',', '.'))
                    produto = float(input('Digite o valor do produto a ser calculado: ').replace(',', '.'))
                    resultado = produto + (produto * dif)
                    resultado2 = resultado + (resultado * margem)
                    resultado3 = resultado2 + (resultado2 * imposto)
                    resultadof = resultado3 + ipi
                    print('O valor final do seu produto é: {:.3f}'.format(resultadof))
                    print('--' * 50)
                    del produto
            elif resposta in ['N', 'n']:
                while True:
                    produto = float(input('Digite o valor do produto a ser calculado: ').replace(',', '.'))
                    resultado = produto + (produto * dif)
                    resultado2 = resultado + (resultado * margem)
                    resultadof = resultado2 + (resultado2 * imposto)
                    print('O valor final do seu produto é: {:.3f}'.format(resultadof))
                    print('--' * 50)
                    del produto
            else:
                break
    except:
        print('Comando invalido, tente novamente.')


while True:
    entrada()
