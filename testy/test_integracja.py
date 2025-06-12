import csv, json
from pathlib import Path
import pytest

from symulator.dystrybutor_paliwa import DystrybutorPaliwa
from symulator.historia import zapisz_do_csv, zapisz_do_xml, wczytaj_z_json

def test_integracja_zapis_csv_i_xml_i_odczyt_json(tmp_path):
    dp = DystrybutorPaliwa(1, 'ON', 100)
    tx = dp.wydaj(10, 5.0)
    transakcje = dp.pobierz_historie()

    csv_path = tmp_path / "t.csv"
    xml_path = tmp_path / "t.xml"
    json_path = tmp_path / "t.json"

    zapisz_do_csv(transakcje, str(csv_path))
    zapisz_do_xml(transakcje, str(xml_path))

    # sprawdź CSV
    with open(csv_path, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
    assert rows[0] == ['id','paliwo','ilosc','cena_litr','cena_calkowita','czas']
    assert rows[1][0] == '1'
    assert float(rows[1][2]) == 10.0

    # zapisz i wczytaj JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump([{
            "id_dystrybutora": tx.id_dystrybutora,
            "rodzaj_paliwa": tx.rodzaj_paliwa,
            "ilosc": tx.ilosc,
            "cena_za_litr": tx.cena_za_litr,
            "cena_calkowita": tx.cena_calkowita,
            "czas": tx.czas.isoformat()
        }], f)

    dane = wczytaj_z_json(str(json_path))
    assert isinstance(dane, list)
    assert dane[0]["ilosc"] == 10
