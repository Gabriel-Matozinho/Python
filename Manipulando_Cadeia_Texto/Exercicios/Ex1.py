Exercício Python 01: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.split()
print(f'Seu nome em maiúsculo é {nome.upper()} ')
print(f'Seu nome em minúsculo é {nome.lower()} ')
print(f'Seu nome tem ao todo {len(nome)} ')
print(f'Seu primeiro nome é {n1[0]} e ele tem {len(n1[0])}')
