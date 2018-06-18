import primes_times_table
import re


def test_primes_generator():
    assert [n for n in primes_times_table.genprimes(0)] == []
    assert [n for n in primes_times_table.genprimes(1)] == [2]
    assert [n for n in primes_times_table.genprimes(5)] == [2, 3, 5, 7, 11]


def test_cli_tool(capsys):
    """
    Expected STDOUT formatting:
    Multiplication table for first [1] primes:
      2
    2 4
    """
    argv = ['genprimes', '1']
    primes_times_table.main(argv)
    out, err = capsys.readouterr()
    assert err == ''
    assert re.findall(r"^\s+2$", out, re.MULTILINE)
    assert re.findall(r"^\s+2\s+4$", out, re.MULTILINE)
