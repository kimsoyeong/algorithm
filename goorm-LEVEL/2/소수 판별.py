import math

N = int(input())

isPrime = True

primes = [2]

for i in range(2, int(math.sqrt(N))+1):
	if N%i == 0:
		isPrime = False
		break

print(isPrime)