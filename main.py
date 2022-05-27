import time
print('==' * 40)
print('Olá, bem vindo ao script de cálculos  ')
print('==' * 40)
time.sleep(2)
vt = float(input('Digite o valor total da Nota Fiscal:   '))
vp = float(input('Digite o valor dos produtos da Nota Fiscal:  '))
frete = float(input('Digite o valor do frete:   '))
vt2 = frete + vt
dif = (vt2 - vp) / vp
margem = float(input('Digite o valor da margem de lucro. (Ex.: 41% = 0.41)   '))
imposto = float(input('Deseja acrescentar algum valor fixo em % de imposto?  '))
print('==' * 40)
while True:
    produto = float(input('Digite o valor do produto a ser calculado: '))
    resultado = produto + (produto * dif)
    resultado2 = resultado + (resultado * margem)
    resultadof = resultado + (resultado2 * imposto)
    print('==' * 40)

    print('O valor final do seu produto é: {:.3f}'.format(resultadof))
    print('==' * 40)
    del produto
