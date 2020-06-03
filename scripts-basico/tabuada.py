n = int(input('Digite um número para ver sua tabuada: '))
cont = 1
while cont < 11:
    print(f'{n:^2} x {cont:^4} = {n * cont:^2}')
    cont += 1