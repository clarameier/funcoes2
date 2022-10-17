#exemplo1
def contador(inicio , fim, passo):
    c = inicio
    while c <= fim:
        print(f'{c}', end=' ')
        c += passo
    print()

contador(2,10,2)

print('='*100)

#exemplo2
def contador(i, f, p): #função contador
    """
    -> faz uma contagem e mostra na tela.
    i: início da contagem
    f: fim da contagem
    p: passo a passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('fim')

help(contador) #mostra qual é a função que criamos (o contador neste exemplo)

print('='*100)

#exemplo3
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma dos números do programa valem {s}.')

somar(3, 2, 5)
somar(8, 4)
somar(4)
somar()

print('='*100)

#exemplo4
def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}.')

n1 = 2
funcao()
print(f'n1 fora vale {n1}.')

print('='*100)

#exemplo5
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.')

print('='*100)

#exemplo6
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

print('-'*100)


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')

print('='*100)

#exemplo7
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')