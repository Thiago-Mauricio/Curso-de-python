from unidecode import unidecode
f = input('Digite uma frase: ').strip()
F = unidecode(f.upper())
print(f'A letra "A" aparece {F.count("A")} vezes nesta frase. ')
print(f'A letra "A" aparece pela primeira vez na posição {F.find("A")+1}.')
print(f'A letra "A" aparece pela ultima vez na posição {F.rfind("A")+1}. ')