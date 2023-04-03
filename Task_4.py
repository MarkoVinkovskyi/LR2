K = int(input())
Total = list(filter(lambda K: K > 999, range(K, 10000, K)))
print(sum(Total))