import sieve

def test_1():
    s = sieve.sieve()
    i = iter(s)
    assert i.next() == 3

def test_2():
    s = sieve.sieve()
    i = iter(s)
    i.next()
    assert i.next() == 5

def test_3():
    s = sieve.sieve()
    i = iter(s)
    i.next()
    i.next()
    assert i.next() == 7

test_1()
test_2()
test_3()