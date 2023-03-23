x = float(input())
eps = 1e-6
n = 1
sum_n = 1.0
# ищем максимальное n, при котором сумма меньше x
while sum_n - x < eps:
    n += 1
    sum_n += 1.0 / n
m = 1
sum_m = 1.0
# ищем минимальное m, при котором сумма больше x
while x - sum_m > eps:
    m += 1
    sum_m += 1.0 / m
# выводим результаты
print(n - 1, m)
