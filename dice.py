# Criando um simulador de dados
from random import randint
from time import sleep

# Programa
print('======== DADO VIRTUAL ========')
num = int(input('Quantidades de lados que terá o dado: '))

while True:

    op = str(input('Rolar dado [S/N]? '))

    if op.lower() == 's':
        dado = randint(1, num)
        print(f'Valor do dado: {dado}')
        print('------------------------------------')
    else:
        break

print('Fim do programa...')
