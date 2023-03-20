K=int(input())
max_num = (9999 // K) * K
min_num = K - (1000 % K) + 1000
n = (max_num - min_num) // K + 1
sum = (min_num + max_num) * n // 2
print(sum)
