import math
def calculate_years(N, P, M, c=0):
    """
    Рассчитывает, через сколько лет вклад составит не менее M долларов.
    N - начальная сумма вклада
    P - годовой процентный доход
    M - минимальная сумма вклада для достижения
    c - количество лет, прошедших с момента начала вклада
    """
    if N >= M:
        return c
    else:
        N = N + N * (P / 100)
        N = math.floor(N*100)/100
        return calculate_years(N, P, M, c + 1)

N, P, M = map(int, input().split())
years = calculate_years(N, P, M)
print(years)
