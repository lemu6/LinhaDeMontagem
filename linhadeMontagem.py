def linha_de_montagem(a1, a2, t1, t2, e1, e2, x1, x2, n):
    f1 = [0] * (n + 1)
    f2 = [0] * (n + 1)
    l1 = [0] * n
    l2 = [0] * n

    # Inicialização
    f1[1] = e1 + a1[0]
    f2[1] = e2 + a2[0]

    # Cálculo dos tempos mais rápidos
    for j in range(2, n + 1):
        c1 = f1[j-1] + a1[j-1]
        c2 = f2[j-1] + t2[j-2] + a1[j-1]
        if c1 <= c2:
            f1[j] = c1
            l1[j-1] = 1  # Marcar a escolha de continuar na linha 1
        else:
            f1[j] = c2
            l1[j-1] = 2  # Marcar a escolha de mudar da linha 2 para a 1

        c1 = f2[j-1] + a2[j-1]
        c2 = f1[j-1] + t1[j-2] + a2[j-1]
        if c1 <= c2:
            f2[j] = c1
            l2[j-1] = 2  # Marcar a escolha de continuar na linha 2
        else:
            f2[j] = c2
            l2[j-1] = 1  # Marcar a escolha de mudar da linha 1 para a 2

    # Determinar o tempo mínimo final
    if f1[n] + x1 <= f2[n] + x2:
        f_star = f1[n] + x1
        linha_star = 1
    else:
        f_star = f2[n] + x2
        linha_star = 2

    # Reconstruir o caminho ótimo
    caminho_otimo = [linha_star]
    for j in range(n-1, 0, -1):
        if linha_star == 1:
            linha_star = l1[j]
        else:
            linha_star = l2[j]
        caminho_otimo.insert(0, linha_star)

    return f_star, caminho_otimo

# Exemplo de uso
a1 = [7, 9, 3, 4, 8, 4]
a2 = [8, 5, 6, 4, 5, 7]
t1 = [2, 3, 1, 3, 4]
t2 = [2, 1, 2, 2, 1]
e1, e2 = 2, 4
x1, x2 = 3, 2
n = len(a1)

resultado, caminho_otimo = linha_de_montagem(a1, a2, t1, t2, e1, e2, x1, x2, n)
print("Tempo total mínimo:", resultado)
print("Caminho ótimo:", caminho_otimo)
