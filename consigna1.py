A= {101, 102, 103, 104, 105, 106}
B= {104, 105, 106, 107, 108}
C= {102, 105, 109}
#Usuarios que usan ambas plataformas
ambas= {x for x in A if x in B}
#Usuarios que utilizan al menos una
alMenosUna= A | B
#Usuarios que no presentan errores
sinErrores= {x for x in (A | B) if x not in C}
#Usuarios que usan una sola plataforma
a1= A - B
a2= B - A
resultado= a1 | a2
print(f"Los usuarios que utilizan ambas plataformas son: {ambas}")
print(f"Los usuarios que utilizan al menos una plataforma son: {alMenosUna}")
print(f"Los usuarios que no presentan errores son: {sinErrores}")
print(f"Los usuarios que usan una sola plataforma son: {resultado}")
detectados= C - (A | B)
print(f"Los detectados son: {detectados}")