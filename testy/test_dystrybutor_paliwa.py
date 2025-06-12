import pytest
from symulator.dystrybutor_paliwa import DystrybutorPaliwa, BladDystrybutora

def test_wydaj_powodzenie():
    dp = DystrybutorPaliwa(1,'ON',100)
    tx = dp.wydaj(10, 5.0)
    assert dp.pojemnosc == 90
    assert tx.cena_calkowita == 50.0

def test_wydaj_brak_paliwa():
    dp = DystrybutorPaliwa(1,'ON',5)
    with pytest.raises(BladDystrybutora):
        dp.wydaj(10, 5.0)
