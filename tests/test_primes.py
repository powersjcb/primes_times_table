import nprimes


def test_primes_generator():
    assert [n for n in nprimes.genprimes(0)] == []
    assert [n for n in nprimes.genprimes(1)] == [2]
    assert [n for n in nprimes.genprimes(5)] == [2, 3, 5, 7, 11]
