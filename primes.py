from math import sqrt,ceil
primes = [2]
number = 2

Nprimes = int(input("How many primes do you want to calculate? "))

while len(primes) <Nprimes:
    IsPrime = True
    i = 0
    while i < ceil(sqrt(len(primes))) and IsPrime:
        if not number % primes[i]:
            IsPrime = False
        i+=1
    if IsPrime:
        primes.append(number)
    number+=1

print("The first {} primes are: ".format(Nprimes) + str(primes).replace("[","").replace("]",""))