from datetime import date

todays_date = date.today() 
atual = todays_date.year()

nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc

print(f'Se você nasceu em {nasc}, então tem {idade} anos. Logo, seu voto é ', end='')

def voto(negado, opcional, obrigatorio):
    if idade <= 15:
        print('negado.')
    elif 16 <= idade >= 17:
        print('opcional.')
    else:
        print('obrigatório.')
