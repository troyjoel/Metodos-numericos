# Tema 1: Errores
## Subtema: Acumulación de errores

---

## Descripción
Errores pequeños se van acumulando al repetir muchas operaciones, generando resultados cada vez más imprecisos.

---

## Código 1

### Código
```python
s = 0 for i in range(10000):
s += 0.1
print(s)
```

### Resultado
999.9999999999062

---

## Código 2

### Código
```python
s = 0 for i in range(5000):
s += 0.2
print(s)
```

### Resultado
999.9999999999782

---

## Código 3

### Código
```python
s = 0 for i in range(2000):
s += 0.3
print(s)
```

### Resultado
600.0000000000114

---

## Código 4

### Código
```python
s = 0 for i in range(3000):
s += 0.15
print(s)
```

### Resultado
449.99999999999994

---

## Código 5

### Código
```python
s = 0 for i in range(1000):
s += 0.05
print(s)
```

### Resultado
49.9999999999993
