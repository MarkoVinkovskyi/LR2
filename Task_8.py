X = float(input())
M=0
N=0
K=0
while K < X:
   N = N + 1
   K=K+(1/N)
M=N
while 1:
   if K<=X:
      M = M + 1
      K = K + (1 / M)
   else:
      break
print((N-1),(M))