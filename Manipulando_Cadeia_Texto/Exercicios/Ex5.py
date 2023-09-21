Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

palavra = str(input('Digite uma palavra: ')).upper().strip()
print(f'A letra "A" aparece {palavra.count("A")}, aparece pela 1ª vez na posição {palavra.find("A")+1} e na pela última vez na posição {palavra.rfind("A")+1}')
