# Tema 1: Errores
## Subtema: Pérdida de precisión por magnitud

---

## Descripción
Ocurre cuando un número muy pequeño se suma a uno muy grande y el pequeño se pierde debido a la limitada precisión del tipo de dato.

---

## Código 1

### Código

```python
print(1e15 + 1)
```

### Resultado

1000000000000000.0

---

## Código 2

### Código

```python
print(9e16 + 3)
```

### Resultado
9e+16

---

## Código 3

### Código

```python
print(5e14 + 2)
```
### Resultado

500000000000000.0

---

## Código 4

### Código

```python
print(7e17 + 4)
```

### Resultado

7e+17

---

## Código 5

### Código

```python
print(1e16 + 5)
```
### Resultado

10000000000000000.0
