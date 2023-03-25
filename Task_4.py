K = int(input())
sum = 0
for num in range(K, 10000, K):
    if num>999:
        sum += num
print(sum)
