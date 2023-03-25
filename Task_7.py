import math
N,P,M = map(int,input().split())
c=0
while N<M:
   N=N+N*(P/100)
   N = math.floor(N * 100) / 100  # округляем до 2 знаков после запятой
   c +=1
print(c)
