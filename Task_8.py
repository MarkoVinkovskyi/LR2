X = float(input())
M=0
N=0
K=0
while K < X:
   N = N + 1
   K=K+(1/N)

if K > X:
   M=N+1
else: M=N+2
print((N-1),(M-1))
