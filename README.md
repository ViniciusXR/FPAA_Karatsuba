# FPAA_Karatsuba
Programa desenvolvido em Python que implementa o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros. 

# Implementação do Algoritmo de Karatsuba em Python

O **Algoritmo de Karatsuba** é um método eficiente para multiplicação de números inteiros grandes, desenvolvido por Anatolii Alexeevitch Karatsuba em 1960. Este algoritmo utiliza a estratégia "divide e conquista" para reduzir a complexidade da multiplicação de números grandes de O(n²) para O(n^log₂3) ≈ O(n^1.585).

## O que é o Algoritmo de Karatsuba

O algoritmo de Karatsuba é baseado na observação de que dois números de n dígitos podem ser multiplicados usando no máximo 3 multiplicações de números com n/2 dígitos, ao invés de 4 multiplicações como no método tradicional. Esta redução no número de operações leva a uma melhoria significativa na eficiência para números grandes.

### Complexidade Assintótica

- **Complexidade Tradicional:** O(n²)
- **Complexidade Karatsuba:** O(n^log₂3) ≈ O(n^1.585)
- **Vantagem:** Significativamente mais eficiente para números grandes

## Funcionamento do Algoritmo

Para dois números X e Y de n dígitos, o algoritmo funciona da seguinte forma:

1. **Divisão:** Divide X e Y em duas partes de aproximadamente n/2 dígitos cada:
   - X = X₁ × 10^(n/2) + X₀
   - Y = Y₁ × 10^(n/2) + Y₀

2. **Conquista:** Calcula três produtos recursivamente:
   - P₁ = X₁ × Y₁
   - P₂ = X₀ × Y₀  
   - P₃ = (X₁ + X₀) × (Y₁ + Y₀)

3. **Combinação:** O resultado final é:
   - X × Y = P₁ × 10^n + (P₃ - P₁ - P₂) × 10^(n/2) + P₂