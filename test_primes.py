import pytest
import math

def is_prime(x):
    return all(x % factor != 0 for factor in range(2, int(x/2)))

@pytest.fixture(params=[2,3,5,7,11, 13, 17, 19, 101])
def prime_number(request):
    return request.param

def test_prime(prime_number):
    assert is_prime(prime_number) == True
    
