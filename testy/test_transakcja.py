import pytest
from symulator.transakcja import Transakcja
from datetime import datetime

def test_transakcja_repr():
    czas = datetime(2025, 6, 13, 12, 0)
    t = Transakcja(1, 'ON', 10.0, 5.5, czas)
    rep = repr(t)
    assert 'dystrybutor=1' in rep
    assert 'ilosc=10.0' in rep
    assert 'razem=55.0' in rep
