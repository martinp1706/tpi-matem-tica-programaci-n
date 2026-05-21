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
#Logica Proporcional 
todos = A | B | C
criticos = []
no_criticos = []
for usuario in todos:
    p = usuario in A
    q = usuario in B
    r = usuario in C
    if (p or q) and r:
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)
print(f"Los usuarios críticos son: {criticos}")
print(f"Los usuarios no críticos son: {no_criticos}")
#tabla de verdad 
print("TABLA DE VERDAD")
print("p q r resultado")
valores = [True, False]
for p in valores:
    for q in valores:
        for r in valores:
            resultado = (p or q) and r
            print(p, q, r, resultado)
#CONSIGNA 2:
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


import math


pendiente_a=40
ordenada_origen_a=200

print("pendiente_a=",pendiente_a)
print("ordenada_origen_a=",ordenada_origen_a)

pendiente_b=70
ordenada_origen_b=50

print("pendiente_b=",pendiente_b)
print("ordenada_origen_b=",ordenada_origen_b)


if pendiente_a == pendiente_b:
    print("Las rectas son paralelas ")
else:
    print("Las rectas no son paralelas")


x =(ordenada_origen_a-ordenada_origen_b) / ( pendiente_b - pendiente_a)
y = pendiente_a * x + ordenada_origen_a

print("x =",x)
print("y =",y)

print("punto de interseccion")
print("(",x,",",y,")")


#vertice
a=-2
b=80
c=100

xv=-b / (2 * a)

yv=-2 * xv**2 + 80 * xv + 100

print("vertices:")
print("(", xv, ",", yv, ")")


a=1
b=-40
c=-50

x1=(-b - math.sqrt(b**2-4*a*c)) / ( 2 * a)

x2=(-b + math.sqrt(b**2-4*a*c)) / (2 * a)

print("Raiz 1:",x1)
print("Raiz 2:",x2)

if 0 <= x1 <= 50:
    print(x1,"sirve en el problema")
if 0 <= x2 <= 50:
    print(x2,"sirven el problema")
else:
    print(x2,"no sirve en el problema")



pendiente_a=40
ordenada_origen_a=200

print("pendiente_a=",pendiente_a)
print("ordenada_origen_a=",ordenada_origen_a)

pendiente_b=70
ordenada_origen_b=50

print("pendiente_b=",pendiente_b)
print("ordenada_origen_b=",ordenada_origen_b)


if pendiente_a == pendiente_b:
    print("Las rectas son paralelas ")
else:
    print("Las rectas no son paralelas")


x =(ordenada_origen_a-ordenada_origen_b) / ( pendiente_b - pendiente_a)
y = pendiente_a * x + ordenada_origen_a

print("x =",x)
print("y =",y)

print("punto de interseccion")
print("(",x,",",y,")")


a=-2
b=80
c=100

xv=-b / (2 * a)

yv=-2 * xv**2 + 80 * xv + 100

print("vertices:")
print("(", xv, ",", yv, ")")



a=1
b=-40
c=-50

x1=(-b - math.sqrt(b**2-4*a*c)) / ( 2 * a)

x2=(-b + math.sqrt(b**2-4*a*c)) / (2 * a)

print("Raiz 1:",x1)
print("Raiz 2:",x2)

if 0 <= x1 <= 50:
    print(x1,"sirve en el problema")
if 0 <= x2 <= 50:
    print(x2,"sirven el problema")
else:
    print(x2,"no sirve en el problema")
    



import math
import matplotlib.pyplot as Plt



def A(x):
    return 40*x + 200
def B(x):
    return 70*x + 50
def C(x):
    return -2*x**2 + 80*x + 100





print("funcion A")
print("pendiente_a:",40)
print("ordenada_origen_a:",200)

print()

print("funcion B")
print("pendiente_b",70)
print("ordenada_origen_b:",50)

print()



if 40 == 70:
    print("son paralelas:")
else:
    print("no son paralelas:")
    
print()


x= (200 - 50) / (70 - 40)
y= A(x)

print("interseccion")
print("(",x,",",y,")")
print()



a= - 2
b= 80
xv= - 2 / (2 * a)
y= C (xv)

print("vertices:")
print("(",xv,",",yv,")")
print()



a= 2
b=80
c=100
d= b**2 - 4*a*c 

x1= (-b+ math.sqrt(d)) / ( 2 * a)
x2= (-b- math.sqrt(d)) / ( 2 * a)

print("Raiz 1:",x1)
print("Raiz 2:",x2)
print()



valores= [0,5,10,15,20,25,30,40,50]
for x in valores:
    print("x=",x)
    
    print("A=",A(x))
    print("B=",b(x))
    print("C=",C(x))
    print()


def barato (x):
    a= A(x)
    b= B(x)
    c= C(x)
    
    menor= min(a,b,c)
    
    if menor == a:
        return("Plan A")
    
    elif menor == b:
        return ("Plan B")
        
    else:
        return ("Plan C")
        
print("plan mas barato")

for x in valores:
    print(x,"horas ->", barato (X))
    


x=list(range(0,51))

yA=[A(i) for i in x]
yB=[B(i) for i in x]
yC=[C(i) for i in x]

plt.plot(x,yA,label="A")
plt.plot(x,yB,label="B")
plt.plot(x,yC,label="C")

plt.legend()
plt.grid()

plt.show()
    
        


print("ANALISIS DE PLANES")
print()



for x in valores:
    a=A(x)
    b=B(x)
    c=C(x)
    
    menor=min(a,b,c)
    print("x=",x)
    
    if menor== a:
        print("conviene el PLAN A")
        
    elif menor == b:
        print("conviene el PLAN B")
    else:
        print("conviene el PLAN C")
    print()
        


print("valores negativos de C")
print()

for x in range (0,51):
    if C(x) < 0:
        print("en x=",x,"el costo es negativo")
        print("C(x)=",C(x))

print()



print("un costo negativo es un problema real")
print("porque significaria que la empresa")
print("le paga dinero al cliente.")
#CONSIGNA 3:
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
