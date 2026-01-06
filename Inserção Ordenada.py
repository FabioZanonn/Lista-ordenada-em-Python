lista = [5, 8, 10]

novo_numero = int(input('Digite: '))

for valores in range(0, len(lista)):
    if novo_numero <= lista[valores]:
        lista.insert(valores, novo_numero)
        break
    if novo_numero > lista[valores]:
        lista.append(novo_numero)

print(lista)
