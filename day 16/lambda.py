
# x = lambda a, b: a - b
# print(x(4, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
myfourther = myfunc(4)

print(mydoubler(11)) 
print(mytripler(11))
print(myfourther(11))