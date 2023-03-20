N,X=map(int,input().split())
c=1
while N<=X:
    N=N+0.1*N
    c +=1
print(c)
