from math import sqrt,ceil
primes = [2]
number = 2

while len(primes) < 58:
    IsPrime = True
    i = 0
    while i < ceil(sqrt(len(primes))) and IsPrime:
        if not number % primes[i]:
            IsPrime = False
        i+=1
    if IsPrime:
        primes.append(number)
        print(primes)
    number+=1