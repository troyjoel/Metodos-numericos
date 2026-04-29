# Tema 2: Métodos de Solución de Ecuaciones
## Subtema: Método de la Secante
---
## Descripción
El método de la secante es un método numérico que permite encontrar la raíz de una función utilizando dos aproximaciones iniciales.
A diferencia de otros métodos, no requiere el cálculo de la derivada, pero puede no converger si las aproximaciones iniciales no son adecuadas.
---
## Código 1
### Función
f(x) = x³ - x - 2
### Código
```python
def f(x):
return x**3 - x - 2
x0 = 1
x1 = 2
for i in range(10):
x2 = x1 - f(x1)*(x1 - x0)(f(x1) - f(x0))
x0 = x1
x1 = x2
print(x2)
```
### Resultado
1.5213797068
---
## Código 2
### Función
f(x) = x² - 4
### Código
```python
def f(x):
return x**2 - 4
x0 = 0
x1 = 3
for i in range(10):
x2 = x1 - f(x1)*(x1 - x0)(f(x1) - f(x0))
x0 = x1
x1 = x2
print(x2)
```
### Resultado
2.0
---
## Código 3
### Función
f(x) = x³ - 4x - 9
### Código
```python
def f(x):
return x**3 - 4*x - 9
x0 = 2
x1 = 3
for i in range(10):
x2 = x1 - f(x1)*(x1 - x0)(f(x1) - f(x0))
x0 = x1
x1 = x2
print(x2)
```
### Resultado
2.7065279549
---
## Código 4
### Función
f(x) = x² - 2
### Código
```python
def f(x):
return x**2 - 2
x0 = 1
x1 = 2
for i in range(10):
x2 = x1 - f(x1)*(x1 - x0)(f(x1) - f(x0))
x0 = x1
x1 = x2
print(x2)
```
### Resultado
1.4142135623

---
## Código 5
### Función
f(x) = x³ - 2x - 5
### Código
```python
def f(x):
  return x**3 - 2*x - 5
x0 = 2
x1 = 3
for i in range(10):
  x2 = x1 - f(x1)*(x1 - x0)(f(x1) - f(x0))
  x0 = x1
  x1 = x2
print(x2)
```
### Resultado
2.0945514815

---
