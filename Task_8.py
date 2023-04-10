import functools

@functools.lru_cache(maxsize=None)
def calculate_sum(n):
    """
    Вычисляет сумму 1 + 1/2 + 1/3 + ... + 1/n.
    n - количество элементов в сумме.
    """
    if n == 0:
        return 0
    else:
        return calculate_sum(n-1) + 1/n

def find_max_min_numbers(X, eps=1e-6):
    """
    Находит максимальное число N, такое что 1 + 1/2 + 1/3 + ... + 1/N < X,
    и минимальное число M, такое что 1 + 1/2 + 1/3 + ... + 1/M > X.
    X - заданное вещественное число.
    eps - допустимая погрешность при вычислениях.
    """
    N = 0
    K = 0
    while K < X - eps:
        N += 1
        K = calculate_sum(N)
    M = N
    while True:
        if K <= X + eps:
            M += 1
            K = calculate_sum(M)
        else:
            break
    return N-1, M

X = float(input())
N, M = find_max_min_numbers(X)
print(N, M)
