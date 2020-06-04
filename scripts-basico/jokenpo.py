from random import randint
from time import sleep

game = ('Pedra', 'Papel', 'Tesoura')

print('JOKENPOH!')
print("""[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura""")

answer = ''

while answer != 'N':
    computer = randint(0, 3)
    option = int(input('Digite sua opção: '))

    while option != 0 and option != 1 and option != 2:
        option = int(input('Digite uma opção válida: '))

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POH!!!')
    sleep(1)

    print(f'Jogador jogou {game[option]}')
    print(f'Computador jogou {game[computer]}')

    # Jogador jogou PEDRA
    if option == 0 and computer == 0:
        print('EMPATE!!!')
    elif option == 0 and computer == 1:
        print('Computador Venceu !')
    elif option == 0 and computer == 2:
        print('Jogador Venceu !')

    # Jogador jogou PAPEL
    if option == 1 and computer == 0:
        print('Jogador Venceu !')
    elif option == 1 and computer == 1:
        print('EMPATE!!!')
    elif option == 1 and computer == 2:
        print('Computador Venceu !')

    # Jogador jogou TESOURA
    if option == 2 and computer == 0:
        print('Computador Venceu !')
    elif option == 2 and computer == 1:
        print('Jogador Venceu !')
    elif option == 2 and computer == 2:
        print('EMPATE!!!')
    
    answer = str(input('Quer jogar novamente [S/N]: ')).strip().upper()[0]
    while answer not in 'SN':
        answer = str(input('Digite uma opção válida[S/N]: ')).strip().upper()[0]
    if answer == 'N':
        break

print('Obrigado por jogar! Volte Sempre !')