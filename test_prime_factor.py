from prime_factor import PrimeFactor


def test_prime_factor():
    prime_factor = PrimeFactor()
    assert prime_factor is not None
def test_prime_factor_of_1():
    prime_factor = PrimeFactor()

    assert prime_factor.of(1) == []