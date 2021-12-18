from math import sqrt as raizq

import os
from time import sleep

#Cores

vermelho = ('\033[1;31m')

verde = ('\033[1;32m')

ciano = ('\033[1;90m')

branco = ('\033[1;97m')

azul = ('\033[1;34m')

########
os.system("cls" if os.name == "nt" else "clear")
import time
def espera():
	frames = [
		"🕛",
		"🕐",
		"🕑",
		"🕒",
		"🕓",
		"🕔",
		"🕕",
		"🕕",
		"🕖",
		"🕗",
		"🕘",
		"🕙",
		"🕚",
		"🕛"
	]

	for i in frames:
		print("Carregando " + str(i), end="\r")
		time.sleep(0.1)


count = 0
while count < 10:
	espera(); count += 1
print(f'''{verde}
pronto!''')
sleep(2)
os.system("cls" if os.name == "nt" else "clear")

print('''
░░░░░░░░░░ ★
░░░░░░░░░░███
░░░░░░░░░█████
░░░░░░░██▒▒▒▒██
░░░░░██▒▒▒▒▒▒▒▒██
░░░░░░░██▒▒▒▒██
░░░░░░░░██████
░░░░░░░███▓▓███
░░░░░░░░█▓▓▓▓█
░░░░░░░█▓▓▓▓▓▓█
░░░░░░█▓▓▓▓▓▓▓▓█
░░░░░█▓▓▓▓▓▓▓▓▓▓█
░░░████▓▓▓▓▓▓▓▓████
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
░███████▓▓▓▓▓▓███████
░░░░░░█▓▓▓▓▓▓▓▓█
░░░░░█▓▓▓▓▓▓▓▓▓▓█
░░░░█▓▓▓▓▓▓▓▓▓▓▓▓█
░░███▓▓▓▓▓▓▓▓▓▓▓▓███
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
███████▓▓▓▓▓▓▓▓███████
░░░░█▓▓▓▓▓▓▓▓▓▓▓▓█
░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██████████████████████
░░░░░░░░██████
''')
print(f'{azul}Feliz Natal!!!')
sleep(3)
os.system("cls" if os.name == "nt" else "clear")
print('''
╔════•ೋೋ•════╗ 
  Calculadora
╚════•ೋೋ•════╝
''')
print(f'''
{vermelho}1 = Adição (+)
{branco}2 = Subtração (-)
{ciano}3 = Multiplicação (×)
{azul}4 = Divisão (÷)
{verde}5 = Calcular raíz quadrada
{branco}6 = Par ou impar?
{vermelho}7 = Dúvidas
{ciano}8 = sair
''')

pg = int(input(f'{verde}Escolha uma das opções acima: '))
if pg == (1):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Adição ==========')
        m1 = int(input(f'{branco}Digite um valor: '))
        m2 = int(input(f'{azul}Digite outro valor: '))
        rm = (m1 + m2)
        print(f'{azul}A soma entre {vermelho}{m1}{vermelho} + {branco}{m2}{azul} dá: {verde}{rm}')
        print(f'''
{verde}1 - Sim 
{vermelho}2 - Não
''')
        pg1 = int(input(f'{branco}Deseja realizar um novo cáluculo?: '))
        if pg1 == (1):
            continue
        else:
            print('Bye')
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            break
elif pg == (2):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Subtração ==========')
        s1 = int(input(f'{branco}Digite um valor: '))
        s2 = int(input(f'{azul}Digite outro valor: '))
        rs = (s1 - s2)
        print(f'A subtração entre {vermelho}{s1}{azul} - {branco}{s2}{azul} dá: {verde}{rs}')
        print(f'''
{verde}1 - Sim 
{vermelho}2 - Não
''')
        pg2 = int(input(f'{branco}Deseja realizar um novo cáluculo?: '))
        if pg2 == (1):
            continue
        elif pg2 == (2):
            print('Bye')
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            break
elif pg == (3):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Multiplicação ==========')
        p1 = int(input(f'{branco}Digite um valor: '))
        p2 = int(input(f'{azul}Digite outro valor: '))
        rp = (p1 + p2)
        print(f'{vermelho}A resposta da multiplicação entre {ciano}{p1}{azul} - {verde}{p2}{azul} é: {rp}')
        print(f'''
{verde}1 - Sim
{vermelho}2 - Não
        ''')
        pg3 = int(input(f'{branco}Deseja realizar um novo cáluculo?: '))
        if pg3 == (1):
            continue
        elif pg3 == (2):
            print('Bye')
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            break
elif pg == (4):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Divisão ==========')
        d1 = int(input(f'{branco}Digite um valor: '))
        d2 = int(input(f'{azul}Digite outro valor: '))
        rd = (d1 // d2)
        rd1 = (d1 % d2)
        if rd1 == 0:
            print(f'A divisão entre {ciano}{d1}{azul} ÷ {vermelho}{d2}{azul} dá: {branco}{rd}.')
        else:
            print(f'{azul}A divisão entre {ciano}{d1}{azul} ÷ {vermelho}{d1}{azul} é igual a: {branco}{rd}{azul} e tem como resto: {branco}{rd1}.')
        print(f'''
{verde}1 - Sim
{vermelho}2 - Não
        ''')
        pg4 = int(input(f'{branco}Deseja realizar um novo cáluculo?: '))
        if pg4 == (1):
            continue
        elif pg4 == (2):
            print('Bye')
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            break
elif pg == (5):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Raíz Quadrada ==========')
        r1 = int(input(f'{branco}Digite um número: '))
        r2 = raizq(r1)
        print(f'{azul}A raíz quadrada de {vermelho}{r1}{azul} é: {branco}{r2}')
        sleep(4)
        print(f'''
{verde}1 - Sim
{vermelho}2 - Não''')
        pg5 = int(input('Deseja realizar um novo calculo?: '))
        if pg5 == (1):
            continue
        elif pg5 == (2):
            print('Bye')
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            break
elif pg == 6:
    while True:      
        os.system("cls" if os.name == "nt" else "clear")
        print(f'{ciano}========= Par ou Ímpar? ==========')
        p1 = int(input('Digite um valor: '))
        rp = (p1 % 2)
        if rp == 0:
            print(f'{azul}O número {branco}{p1}{azul} é par.')
        else:
            print(f'{azul}O número {branco}{p1}{azul} é ímpar.')
        print(f'''
{verde}1 - Sim
{vermelho}2 - Não''')
        pg6 = int(input('Deseja fazer um novo cálculo?: '))
        if pg6 == 1:
            continue
        elif pg6 == 2:
            print(f'bye')
            sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            break
elif pg == 7:
    os.system("cls" if os.name == "nt" else "clear")
    print(f'''{branco}Essa é uma nova
{ciano}calculadora{branco}, com {ciano}sistemas{branco} e {ciano}design{branco}
reformados e bem mais funcionais e
bonitos.''')
    pg7 = input('Digite qualquer coisa pra sair: ')
elif pg == 8:
    os.system("cls" if os.name == "nt" else "clear")
    exit()