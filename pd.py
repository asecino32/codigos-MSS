def DPMSS(A):
    n = len(A)
    MSS = [[0] * n for _ in range(n)]  # matriz n×n inicializada en 0

    # Caso base: subarreglos de tamaño 1
    for i in range(n):
        MSS[i][i] = A[i]

    # len = longitud del subarreglo - 1
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            max_val = float('-inf')

            # Probar todas las particiones k
            for k in range(i, j):
                max_val = max(
                    max_val,
                    MSS[i][k],
                    MSS[k + 1][j],
                    MSS[i][k] + MSS[k + 1][j]
                )

            MSS[i][j] = max_val

    return MSS[0][n - 1]

def MSS(A, memo=None):
    if memo is None:
        memo = {}

    n = len(A)
    if n == 0:
        return 0

    # Si ya lo calculamos, devolvemos el resultado guardado
    if n in memo:
        return memo[n]

    # Calculamos el máximo entre incluir o no el último elemento
    sum1 = MSS(A[:-1], memo)          # sin incluir A[n]
    sum2 = MSS(A[:-1], memo) + A[-1]  # incluyendo A[n]

    memo[n] = max(sum1, sum2)
    return memo[n]


A=[5,2,-1,-7, 9,-2,4,5,2,-1,-7, 9,-2,4,5,2,-1,-7, 9,-2,4,5,2,-1,-7, 9,-2,4,5,2,-1,-7, 9,-2,4]
print(DPMSS(A))
print(MSS(A))