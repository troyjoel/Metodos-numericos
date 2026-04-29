# Tema 2: Métodos de Solución de Ecuaciones

---

## Descripción General
Los métodos de solución de ecuaciones permiten encontrar valores aproximados de las raíces de una función, es decir, los puntos donde f(x) = 0.

Estos métodos son utilizados cuando no es posible resolver una ecuación de manera exacta mediante procedimientos algebraicos.

Se basan en procesos iterativos que generan aproximaciones sucesivas hasta alcanzar un resultado con la precisión deseada.

---

## Método de Bisección

Es un método que consiste en dividir repetidamente un intervalo en dos partes iguales y seleccionar el subintervalo donde existe un cambio de signo en la función.

Garantiza la convergencia si la función es continua en el intervalo.

Fórmula:
c = (a + b) / 2

---
```python
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
```
---

## Método de Falsa Posición

También conocido como método de la regla falsa, utiliza una recta secante entre dos puntos del intervalo para aproximar la raíz de la función.

Puede ser más eficiente que el método de bisección al considerar la forma de la función.

Fórmula:
c = b - f(b)(a - b) / (f(a) - f(b))

---
```python
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
```
---

## Método de la Secante

Este método utiliza dos aproximaciones iniciales para generar una nueva aproximación mediante una recta secante.

No requiere que exista un cambio de signo, pero no siempre garantiza convergencia.

Fórmula:
xₙ₊₁ = xₙ - f(xₙ)(xₙ - xₙ₋₁) / (f(xₙ) - f(xₙ₋₁))

---
```python
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
```
---

## Método de Newton-Raphson

Es un método iterativo que utiliza la derivada de la función para calcular aproximaciones sucesivas de la raíz.

Es uno de los métodos más rápidos, pero requiere conocer la derivada y una buena aproximación inicial.

Fórmula:
xₙ₊₁ = xₙ - f(xₙ) / f'(xₙ)

---
```python
def f(x):
    return x**2 - 4  # cambia función

def df(x):
    return 2*x       # cambia derivada

x = float(input("Valor inicial: "))
tol = float(input("Tolerancia: "))

while True:
    x_new = x - f(x)/df(x)

    if abs(x_new - x) < tol:
        break

    x = x_new

print("Raíz aproximada:", x_new)
```
---
