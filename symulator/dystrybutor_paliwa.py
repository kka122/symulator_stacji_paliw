from datetime import datetime
from .transakcja import Transakcja

class BladDystrybutora(Exception):
    """Brak paliwa lub nieprawidłowa ilość."""
    pass

class DystrybutorPaliwa:
    def __init__(self, id: int, rodzaj_paliwa: str, pojemnosc: float):
        assert pojemnosc >= 0, "Pojemność musi być ≥ 0"
        self.id = id
        self.rodzaj_paliwa = rodzaj_paliwa
        self.pojemnosc = pojemnosc
        self.historia = []  # lista Transakcja

    def wydaj(self, ilosc: float, cena_za_litr: float) -> Transakcja:
        if ilosc <= 0:
            raise ValueError("Ilość musi być dodatnia")
        if ilosc > self.pojemnosc:
            raise BladDystrybutora(f"Dostępne tylko {self.pojemnosc} L")
        self.pojemnosc -= ilosc
        t = Transakcja(self.id, self.rodzaj_paliwa, ilosc, cena_za_litr, datetime.now())
        self.historia.append(t)
        return t

    def pobierz_historie(self):
        return self.historia

# Przykład dziedziczenia
class DystrybutorElektryczny(DystrybutorPaliwa):
    """KWh zamiast litrów."""
    def __init__(self, id: int, pojemnosc_kwh: float):
        super().__init__(id, 'electric', pojemnosc_kwh)
