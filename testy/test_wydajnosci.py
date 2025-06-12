import timeit
from memory_profiler import memory_usage
import pytest

from symulator.dystrybutor_paliwa import DystrybutorPaliwa

def test_czas_wydawania():
    dp = DystrybutorPaliwa(1, 'ON', 1_000_000)
    # zmierz 1 000 wywołań
    t = timeit.timeit("dp.wydaj(1, 1.0)", globals={'dp': dp}, number=1000)
    # oczekujemy, że poniżej 0.1s
    assert t < 0.1

def test_pamiec_wydawania():
    dp = DystrybutorPaliwa(2, 'PB', 1_000_000)
    # zmierz przyrost pamięci podczas 1 wywołania
    mem = memory_usage((dp.wydaj, (1, 1.0)), max_usage=True)
    # oczekujemy przyrostu < 1 MiB
    assert mem < 1
