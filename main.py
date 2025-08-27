#Programa desenvolvido em Python que implementa o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.

def karatsuba(x, y):
    # Caso base: se os números são pequenos, usa multiplicação tradicional
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números
    high_x, low_x = divmod(x, 10 ** m)
    high_y, low_y = divmod(y, 10 ** m)

    # Três multiplicações recursivas
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combina os resultados
    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


if __name__ == "__main__":

    print('Algoritmo de Karatsuba')
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))

    resultado = karatsuba(numero1, numero2)

    print('Primeiro número', numero1)
    print('Segundo número', numero2)

    print(f"Resultado: {resultado}")