import time  #Importando bibliotecas

#Criando a funçao dos menus e apresentaçoes


def menu():
    print('==' * 50)
    print('||  Olá, bem vindo ao script de cálculos.                                                         ||')
    print('||  Ao digitar porcentagens digite o numero inteiro (Ex 40,50).                                   ||')
    print('||  Ao digitar numeros decimais, pode utilizar tanto ponto como virgula.                          ||')
    print('||  Caso queira reiniciar os calculos, basta digitar qualquer letra ou palavra.                   ||')
    print('||  Ao calcular ST manualmente favor digitar o valor total dos produtos nos 2 primeiros campos.   ||')
    print('||  Faça bom proveito.                                                                            ||')
    print('==' * 50)
    print('  ')
    print('  ')
    print('  ')
    time.sleep(1)
    opcao = str(input('Digite S para continuar e N para sair: '))
    if opcao.lower() == 's':
        entrada()
    elif opcao.lower() == 'n':
        exit()
    else:
        menu()

#Funçao de entrada de dados e calculo das notas


def entrada():
    try:

        valor_total = float(input('Digite o valor total da Nota Fiscal:   ').replace(',', '.'))
        valor_produtos = float(input('Digite o valor dos produtos da Nota Fiscal:  ').replace(',', '.'))
        frete = float(input('Digite o valor do frete:   ').replace(',', '.'))
        valor_com_frete = frete + valor_total
        quociente = (valor_com_frete - valor_produtos) / valor_produtos
        margem = float(input('Digite a porcentagem da margem de lucro:   ').replace(',', '.')) / 100
        imposto = float(
            input('Digite o valor fixo em % de imposto que será aplicado a todos os produtos:  ').replace(',',
                                                                                                          '.')) / 100

        resposta = (input('Deseja calcular o ST manualmente para cada produto ? (S/N) '))

        if resposta.lower() == 's':
            while True:
                substituicao_tributaria = float(input('Digite o ST do produto:  ').replace(',', '.'))
                if substituicao_tributaria == 'sair':
                    menu()
                else:
                    produto = float(input('Digite o valor do produto a ser calculado: ').replace(',', '.'))
                    if produto == 'sair':
                        menu()
                    else:
                        produto_com_st = substituicao_tributaria + produto
                        resultado_inicio = produto_com_st + (produto_com_st * quociente)
                        resultado_meio = resultado_inicio + (resultado_inicio * margem)
                        resultado_final = resultado_meio + (resultado_meio * imposto)
                        print('O valor final do seu produto é: {:.3f}'.format(resultado_final))
                        print('--' * 50)
                        del produto

        elif resposta.lower() == 'n':
            while True:
                produto = float(input('Digite o valor do produto a ser calculado: ').replace(',', '.'))
                if produto == 'sair':
                    menu()
                else:
                    resultado_inicio = produto + (produto * quociente)
                    resultado_meio = resultado_inicio + (resultado_inicio * margem)
                    resultado_final = resultado_meio + (resultado_meio * imposto)
                    print('O valor final do seu produto é: {:.3f}'.format(resultado_final))
                    print('--' * 50)
                    del produto

        else:
            time.sleep(1)
            print('Dados invalidos, preencha novamente.')

    except ValueError:
        print('Comando invalido, tente novamente.')


while True:
    menu()
