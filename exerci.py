def multiplicar_matrizes(matriz1, matriz2):
    # Verifica se as matrizes podem ser multiplicadas
    if len(matriz1[0]) != len(matriz2):
        return None
# Cria a Matriz 
    n_linhas = len(matriz1)
    n_colunas = len(matriz2[0])
    matriz_resultado = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(0)
        matriz_resultado.append(linha)
    
# Multiplica as Matrizes 
    for i in range(n_linhas):
        for j in range(n_colunas):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            matriz_resultado[i][j] = soma    
    return matriz_resultado
    
#Valores das Matrizes da Atividade 
matriz1 = [[3, 1, 3], [6, 5, 5]]
matriz2 = [[100, 50], [50, 100], [50, 50]]

#Forma de mostra a matriz no final 
print()
print("Matriz Final" )
for linha in multiplicar_matrizes(matriz1,matriz2):
    for matriz_final in linha:
        print(matriz_final, end=' ')
    print()
#Soma todos os valores da Matriz

somafinal = multiplicar_matrizes
soma = 0
for linha in multiplicar_matrizes(matriz1,matriz2):
    for valor in linha:
        soma += valor
print("A soma de todos os botões usados é :", soma)




     

