l=0
k=0
while 1:
   n =int(input())
   if n != 0:
      k = k+n
   elif n == 0 and l == 0:
      l=1
   elif n == 0 and l == 1:
       break
print((k))
