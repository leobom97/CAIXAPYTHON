'''Crie um programa que simule o funcionamento
de um caixa eletrônico.No início,pergunte ao usuário
qual será o valor a ser sacado(número inteiro)e o programa
vai informar quantas cédulas de cada valor serão entregues'''
#OBS:Considere que o caixa possui cédulas R$50, R$20, R$10 e R$1
print('=' * 30)
print('{:^30}'.format('BANCO RODRIGUES'))
print('=' * 30)
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédula += 1
    else:
        if totalcédula > 0:
            print(f'Total de {totalcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédula = 0
        if total == 0:
            break
print('=' * 30)
print('VOLTE SEMPRE AO BANCO RODRIGUES')