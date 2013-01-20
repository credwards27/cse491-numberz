# implementation of the sieve of eratosthenes as a module

# list of all found prime numbers
_primeslist = [2]

# check if a number is prime
# iterate through all numbers in primes list
# modulo divide the current possible prime by all numbers in the primes list
def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

# find the next prime number and add it to the list
# start with the last prime number plus 1
# if the number is prime, add it to the list and return its value
# if it is not prime, check the next consecutive number
def sieve():
    start = _primeslist[-1] + 1
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            
            return start
        
        start += 1
