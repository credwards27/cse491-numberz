# generator implementation of the sieve of eratosthenes

def sieve():
    primes = [2]
    
    # start at the last prime number + 1
    num = primes[-1] + 1
    
    # prime check boolean flag (default true)
    is_prime = True
    
    # check increasing numbers until prime is found
    while 1:
        for i in primes:
            
            # if modulo does not equal 0, not prime
            if num % i == 0:
                is_prime = False
                break
        
        # number is prime if prime flag not changed
        # add number to prime list
        # return the number
        if is_prime == True:
            primes.append(num)
            yield num
        # number is not prime
        # reset prime flag and check next number
        else:
            is_prime = True
            num += 1