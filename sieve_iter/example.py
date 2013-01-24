import sieve

def test(r):
    print 'Running test for', r, 'items'
    
    for n, i in zip(range(r), sieve.sieve()):
        print i
    
    print '\n'

test(5)
test(10)
test(15)