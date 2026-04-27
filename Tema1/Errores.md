# Tema: Tipos de Error en Métodos Numéricos  

---  

## Descripción General  
En los métodos numéricos es fundamental medir qué tan preciso es un resultado.  
Para ello se utilizan diferentes tipos de error que permiten comparar valores aproximados con valores reales.  

---  

## Error absoluto  

El error absoluto es la diferencia en valor entre el dato exacto y el dato aproximado.  
Indica cuánto se aleja el resultado obtenido del valor real sin considerar la escala del número.  

Se utiliza para medir la magnitud directa del error.  

Fórmula:  
Ea = |valor real − valor aproximado|  

---  

## Error relativo  

El error relativo representa el error absoluto en relación con el valor real.  
Permite evaluar la importancia del error considerando el tamaño del número.  

Indica qué tan significativo es el error respecto al valor real.  

Fórmula:  
Er = Ea / valor real  

---  

## Error porcentual  

El error porcentual es el error relativo expresado en porcentaje.  
Se utiliza para interpretar el error de forma más intuitiva y comparar precisión.  

Facilita la interpretación del error en términos porcentuales.  

Fórmula:  
E% = Er × 100  

---
## Código
```python
valor_real = float(input("Ingresa el valor real: "))
valor_aprox = float(input("Ingresa el valor aproximado: "))

# Error absoluto
Ea = abs(valor_real - valor_aprox)

# Error relativo
Er = Ea / valor_real

# Error porcentual
Ep = Er * 100

print("Error absoluto:", Ea)
print("Error relativo:", Er)
print("Error porcentual:", Ep, "%")
```
