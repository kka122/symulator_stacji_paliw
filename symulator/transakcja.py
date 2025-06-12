class Transakcja:
    def __init__(self, id_dystrybutora: int, rodzaj_paliwa: str,
                 ilosc: float, cena_za_litr: float, czas):
        self.id_dystrybutora = id_dystrybutora
        self.rodzaj_paliwa = rodzaj_paliwa
        self.ilosc = ilosc
        self.cena_za_litr = cena_za_litr
        self.cena_calkowita = round(ilosc * cena_za_litr, 2)
        self.czas = czas

    def __repr__(self):
        return (f"<Transakcja dystrybutor={self.id_dystrybutora} "
                f"paliwo={self.rodzaj_paliwa} ilosc={self.ilosc}L "
                f"razem={self.cena_calkowita}zł o {self.czas}>")
