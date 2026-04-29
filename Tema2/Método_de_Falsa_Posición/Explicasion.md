# Tema 2: Métodos de Solución de Ecuaciones
## Subtema: Método de Falsa Posición
---
## Descripción
El método de falsa posición es un método numérico que permite encontrar la raíz de una función utilizando una aproximación basada en una recta secante entre dos puntos.
A diferencia del método de bisección, este método toma en cuenta los valores de la función para mejorar la aproximación, lo que puede hacerlo más rápido en algunos casos.

---
## Código 1
### Función
f(x) = x³ - x - 2
### Código
```python
def f(x):
  return x**3 - x - 2
a = 1
b = 2
for i in range(10):
  c = b - (f(b) * (a - b))  (f(a) - f(b))
if f(a) * f(c) < 0:
  b = c
else:
  a = c
print(c)
```
### Resultado
1.5213767691

---
## Código 2
### Función
f(x) = x² - 4
### Código
```python
def f(x):
  return x**2 - 4
a = 0
b = 3
for i in range(10):
  c = b - (f(b) * (a - b))  (f(a) - f(b))
if f(a) * f(c) < 0:
  b = c
else:
  a = c
print(c)
```
### Resultado
1.9999999181

---
## Código 3
### Función
f(x) = x³ - 4x - 9
### Código
```python
def f(x):
  return x**3 - 4*x - 9
a = 2
b = 3
for i in range(10):
  c = b - (f(b) * (a - b))  (f(a) - f(b))
if f(a) * f(c) < 0:
  b = c
else:
  a = c
print(c)
```
### Resultado
2.7065280545

---
## Código 4
### Función
f(x) = x² - 2
### Código
```python
def f(x):
  return x**2 - 2
a = 1
b = 2
for i in range(10):
  c = b - (f(b) * (a - b))  (f(a) - f(b))
if f(a) * f(c) < 0:
  b = c
else:
  a = c
print(c)
```
### Resultado
1.4142134999

---
## Código 5
### Función
f(x) = x³ - 2x - 5
### Código
```python
def f(x):
  return x**3 - 2*x - 5
a = 2
b = 3
for i in range(10):
  c = b - (f(b) * (a - b))  (f(a) - f(b))
if f(a) * f(c) < 0:
  b = c
else:
  a = c
print(c)
```
### Resultado
2.0945514815

---
