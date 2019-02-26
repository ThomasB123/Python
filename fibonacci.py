a,b=0,1
def fib(a,b):
  if a<1000000:
    a,b=a+b,a
    return str(a) + " " + str(fib(a,b))
  return ""
print (fib(a,b))