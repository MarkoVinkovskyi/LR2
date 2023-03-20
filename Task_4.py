K=int(input())
sum=0
for i in range(K, 10000, K):
     if i>999:
         sum +=i
print(sum)
