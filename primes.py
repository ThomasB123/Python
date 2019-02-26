import time
import math
class Primes():
    def __init__(self):
        self.out = [2,3]
    def first(self,n):
        if n == 1:
            return ([2])
        count,test = len(self.out),self.out[-1]
        if n < count:
            return(self.out[0:n])
        while count < n:
            test += 2
            x = 0
            while x+1 < count and test % self.out[x] != 0 and self.out[x] < math.sqrt(test):
                x += 1
            if test % self.out[x] != 0:
                count += 1
                self.out.append(test)
        return self.out
Primes = Primes()

start = time.time()
prime = (Primes.first(10000))
end = time.time()
print(end-start)
