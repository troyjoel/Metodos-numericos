def f(x):
    return x**2 - 4  # puedes cambiar la función

a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
tol = float(input("Tolerancia: "))

while (b - a) / 2 > tol:
    xm = (a + b) / 2
    
    if f(a) * f(xm) < 0:
        b = xm
    else:
        a = xm

print("Raíz aproximada:", xm)
