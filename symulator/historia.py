import csv, json, xml.etree.ElementTree as ET
from functools import reduce
from matplotlib import pyplot as plt

def zapisz_do_csv(transakcje, sciezka=r'C:\Users\Komputer\Desktop\Politechnika\2_rok\2_semestr\jezyki_skryptowe\symulator_stacji_paliw\dane\transakcje.csv'):
    with open(sciezka, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id','paliwo','ilosc','cena_litr','cena_calkowita','czas'])
        for t in transakcje:
            writer.writerow([t.id_dystrybutora, t.rodzaj_paliwa,
                             t.ilosc, t.cena_za_litr,
                             t.cena_calkowita, t.czas.isoformat()])

def zapisz_do_xml(transakcje, sciezka=r'C:\Users\Komputer\Desktop\Politechnika\2_rok\2_semestr\jezyki_skryptowe\symulator_stacji_paliw\dane\transakcje.xml'):
    root = ET.Element('transakcje')
    for t in transakcje:
        el = ET.SubElement(root, 'transakcja')
        for pole, val in [
            ('id', t.id_dystrybutora), ('paliwo', t.rodzaj_paliwa),
            ('ilosc', t.ilosc), ('cena_litr', t.cena_za_litr),
            ('cena_calkowita', t.cena_calkowita),
            ('czas', t.czas.isoformat())
        ]:
            child = ET.SubElement(el, pole)
            child.text = str(val)
    ET.ElementTree(root).write(sciezka, encoding='utf-8', xml_declaration=True)

def wczytaj_z_json(sciezka=r'C:\Users\Komputer\Desktop\Politechnika\2_rok\2_semestr\jezyki_skryptowe\symulator_stacji_paliw\dane\transakcje.json'):
    with open(sciezka, encoding='utf-8') as f:
        return json.load(f)

def srednia_cena(transakcje):
    ceny = list(map(lambda t: t.cena_za_litr, transakcje))
    suma = reduce(lambda a,b: a+b, ceny, 0)
    return round(suma/len(ceny), 2) if ceny else 0.0

def rysuj_wykres(transakcje, sciezka=r'C:\Users\Komputer\Desktop\Politechnika\2_rok\2_semestr\jezyki_skryptowe\symulator_stacji_paliw\dane\wykres.png'):
    czasy = [t.czas for t in transakcje]
    ilosci = [t.ilosc for t in transakcje]
    plt.figure()
    plt.plot_date(czasy, ilosci, '-o')
    plt.title('Sprzedaż w czasie')
    plt.xlabel('Czas')
    plt.ylabel('Litry')
    plt.tight_layout()
    plt.savefig(sciezka)
    plt.close()
