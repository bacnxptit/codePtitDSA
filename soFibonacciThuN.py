MOD = 10 ** 9 + 7

def multiply_matrix(A, B):
    C = [[0, 0], [0, 0]]

    C[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD

    C[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD

    C[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD

    C[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    return C



def matrix_pow(M, k):
    I = [[1, 0],
         [0, 1]]
    if k == 0:
        return I
    half = matrix_pow(M, k // 2)

    res = multiply_matrix(half, half)

    if k % 2 == 1:
        res = multiply_matrix(res, M)

    return res

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return
    M = [[1, 1],
         [1, 0]]

    result_matrix = matrix_pow(M, n)
    print(result_matrix[0][1])


T = int(input())
for _ in range(T):
    main()