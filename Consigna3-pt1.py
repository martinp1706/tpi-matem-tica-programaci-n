M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

print("PROMEDIO POR FUNCION")

for fila in M:
    promedio = sum(fila) / len(fila)
    print(promedio)


print("PROMEDIO POR SERVIDOR")

columnas = len(M[0])

for j in range(columnas):
    suma = 0

    for i in range(len(M)):
        suma += M[i][j]

    promedio = suma / len(M)
    print(promedio)

    M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

T = []

for j in range(len(M[0])):
    fila = []
    
    for i in range(len(M)):
        fila.append(M[i][j])
    
    T.append(fila)

print(T)