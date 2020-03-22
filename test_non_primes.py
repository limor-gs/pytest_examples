import pytest

FIX_BUG = True
if FIX_BUG:
    def is_prime_fixed(x):
        # notice the +1 - it is important when x=4
        return all(x % factor != 0 for factor in range(2, int(x/2) + 1))
    is_prime = is_prime_fixed
else:
    from test_primes import is_prime

@pytest.fixture(params=[4, 6, 8, 9, 10, 12, 14, 15, 16, 28, 60, 100])
def non_prime_number(request):
    return request.param

def test_non_primes(non_prime_number):
    assert is_prime(non_prime_number) == False
    
