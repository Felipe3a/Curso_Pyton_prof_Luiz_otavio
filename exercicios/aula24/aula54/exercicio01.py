"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')

entrada_int = int(entrada)


if entrada_int % 2 == 0: 
    print(f'O número {entrada_int} é par')
else:
    print(f' {entrada} é impar')
  



  # Pega a entrada do usuário primeiro como texto
entrada_usuario = input('Digite um número inteiro: ')

try:
    # 1. Tenta converter o texto para um número inteiro
    num = int(entrada_usuario)

    # 2. Se a conversão funcionou, o código continua aqui
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        # Corrigido: Se não é par, é ímpar
        print(f'O número {num} é ímpar.')

except ValueError:
    # 3. Se a conversão falhou (porque não era um número),
    #    o Python pula para este bloco
    print(f'"{entrada_usuario}" não é um número inteiro válido.')