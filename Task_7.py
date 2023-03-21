N,P,M = map(int,input().split())
c=0
while N<M:
   N=N+N*(P/100)
   c +=1
print(c)
