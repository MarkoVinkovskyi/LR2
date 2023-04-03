X = float(input())
M=0
N=0
K=0
eps=1e-6

while K < X-eps:
   N = N + 1
   K=K+(1/N)
M=N
while 1:
   if K<=X+eps:
      M = M + 1
      K = K + (1 / M)
   else:
      break
print((N-1),(M))