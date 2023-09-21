Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

1º Modo

nome = str(input('Digite seu nome: ')).upper().strip()
n = nome.split()
print(nome)
print(f'O primero nome é {n[0]}')
print(f'O último nome é {n[-1]}') 

2º Modo

nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print(nome)
print(f'O primero nome é {n[0]}')
print(f'O último nome é {n[len(n)-1]}')'''
