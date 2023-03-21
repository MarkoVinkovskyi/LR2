c=0
k=1001
while 1:
   n =int(input())
   if n != 0:
      if n>k:
         c += 1
      k = n

   elif n == 0:
      break
print(c)
