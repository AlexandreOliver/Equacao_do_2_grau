from time import sleep
print('\033[;;33m='*5,'EQUAÇÃO DO SEGUNDO 2°','='*5,'\033[m')
for r in range(10):
    a = float(input('Variavel A: '))
    if a == 0:
        print("A variavel 'A' deve ser\nobrigatoriamente diferente de [0]")
        sleep(1)
        print("VALOR PARA 'A' INVÁLIDO!")
        print('Tente Novamente')
        sleep(2)
    else:
        break
b = float(input('Variavel B: '))
c = float(input('Variavel C: '))
print('\033[;;33m='*33,'\033[m')
delta = b ** 2 - 4 * a * c
print('Calculando...')
sleep(1)
if delta < 0:
    print('''Para Delta \033[;;31mnegativo\033[m\nnao existe raizes em Reais.
    Delta = {}'''.format(delta))
elif delta > 0:
    print('''Para Delta \033[;;32mpositivo\033[m, a equação possui duas raizes que são:
    Delta = {}'''.format(delta))
    x1 = (-b - (delta ** (1/2))) / (2 * a)
    x2 = (-b + (delta ** (1/2))) / (2 * a)
    print('x1 = {}\nx2 = {}'.format(x1, x2))
elif delta == 0:
    print('''Para delta igual a 0, as raizes são iguais:
    Delta = {}'''.format(delta))
    x2 = (-b + (delta ** (1/2))) / (2 * a)
    print('x1 e x2 = {}'.format(x2))
print('\033[;;33m='*33,'\033[m')