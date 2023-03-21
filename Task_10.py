c=0
k=0
while 1:
   n =int(input())
   if n != 0:
      c +=1
      k = k+n
   elif n == 0:
      break
print((k/c))
