def f(x):
    return x**2 - 4  # cambia función

x0 = float(input("Ingresa x0: "))
x1 = float(input("Ingresa x1: "))
tol = float(input("Tolerancia: "))

while True:
    x2 = x1 - (f(x1)*(x1 - x0)) / (f(x1) - f(x0))

    if abs(x2 - x1) < tol:
        break

    x0 = x1
    x1 = x2

print("Raíz aproximada:", x2)
