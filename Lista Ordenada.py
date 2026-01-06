lista = [8, 7, 5, 5, 11, 3, 9, 11]
print(f'Lista 1: {lista}')

for passadas in range(len(lista)):
    for valores in range(0, (len(lista) - 1)):
        posicao_atual = valores
        proxima_posicao = posicao_atual + 1
        temporario = 0

        if lista[posicao_atual] > lista[proxima_posicao]:
            temporario = lista[proxima_posicao]
            lista[proxima_posicao] = lista[posicao_atual]
            lista[posicao_atual] = temporario

print(f'Lista 2: {lista}')
