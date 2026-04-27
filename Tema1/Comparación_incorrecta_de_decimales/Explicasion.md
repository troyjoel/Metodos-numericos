# Tema 1: Errores
## Subtema: Comparación incorrecta de decimales

---

## Descripción
Comparar números decimales directamente puede fallar debido a pequeños errores de precisión en su representación.

---

## Código 1

### Código
```python
import math
print(math.sqrt(2) * math.sqrt(2) == 2)
```
### Resultado
False

---

## Código 2

### Código
```python
print(0.2 + 0.1 == 0.3)
```

### Resultado
False

---

## Código 3

### Código
```python
import math
print(math.sqrt(3) * math.sqrt(3) == 3)
```

### Resultado
False

---

## Código 4

### Código
```python
print(0.6 - 0.3 == 0.3)
```

### Resultado
False

---

## Código 5

### Código
```python
print(0.5 + 0.2 == 0.7)
```

### Resultado
False
