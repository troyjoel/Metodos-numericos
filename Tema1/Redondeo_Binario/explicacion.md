# Tema 1: Errores
## Subtema: Error de Redondeo Binario

---

##  Descripción
El error de redondeo binario ocurre porque las computadoras representan los números decimales en formato binario, lo que provoca pequeñas imprecisiones en operaciones matemáticas.

---

## Código 1

### Código
```java
public class RedondeoBinario2 {
    public static void main(String[] args) {
        double a = 0.7;
        double b = 0.6;
        System.out.println(a - b);
    }
}
```

### Resultado
0.09999999999999998

