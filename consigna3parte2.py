M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

C = [
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
]

T = []

for i in range(len(M)):

    fila_resultado = []

    for j in range(len(C[0])):

        suma = 0

        for k in range(len(C)):
            suma = suma + M[i][k] * C[k][j]

        fila_resultado.append(suma)

    T.append(fila_resultado)

print("MATRIZ RESULTADO")

for fila in T:
    print(fila)