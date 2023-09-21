Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.

nome = str(input('Digite seu nome: ')).upper().split()
n = 'SILVA' in nome or 'PEREIRA' in nome
print(n)
