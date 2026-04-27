# Tema 1: Errores
## Subtema: Overflow

---

## Descripción
Ocurre cuando un número supera el límite que puede almacenar un tipo de dato.

---

## Código 1

### Código

```python
x = 2000000000
print(x * 2)
```

### Resultado
4000000000

Python no presenta overflow en enteros porque usa precisión arbitraria.
### Resultado en Java
-294967296

---

## Código 2

### Código
```python
x = 2147483647
print(x + 1)
```

### Resultado
2147483648

Python no presenta overflow en enteros.
### Resultado en Java
-2147483648

---

## Código 3

### Código
```python
x = 9223372036854775807
print(x + 1)
```

### Resultado
9223372036854775808

Python maneja correctamente números grandes.
### Resultado en Java
-9223372036854775808

---

## Código 4

### Código
```python
x = 3.4e38
print(x * 10)
```

### Resultado
inf

Aquí sí ocurre overflow en números de punto flotante.

---

## Código 5

### Código
```python
x = 1e308
print(x * x)
```

### Resultado
inf

El valor supera el límite máximo de un float en Python.
