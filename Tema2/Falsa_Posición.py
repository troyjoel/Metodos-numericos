def f(x):
    return x**2 - 4  # puedes cambiar la función

a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
tol = float(input("Tolerancia: "))

xr = a

while True:
    xr_old = xr
    xr = b - (f(b)*(a - b)) / (f(a) - f(b))

    if abs(xr - xr_old) < tol:
        break

    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr

print("Raíz aproximada:", xr)
