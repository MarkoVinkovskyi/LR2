num=int(input())
binary=(bin(num))
a = str(binary)
print(a[1:].count('0'))