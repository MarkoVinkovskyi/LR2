c=0
k=0
while 1:
   n =int(input())
   if n != 0:
      if abs(n)>abs(k):
         c = n
      k = n
   elif n == 0:
      break
print(c)
