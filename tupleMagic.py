def add(a,b):
 return a+b

print(add(2,3))
t = (3,5)
print(add(*t))

a,b,*rest = range(10)
a,*rest,b = range(5)
