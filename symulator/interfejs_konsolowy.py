from .dystrybutor_paliwa import DystrybutorPaliwa, BladDystrybutora
from .historia import (zapisz_do_csv, zapisz_do_xml,
                       srednia_cena, rysuj_wykres)

def pokaz_menu():
    print("=== Symulator stacji paliw ===")
    print("1. Wydaj paliwo")
    print("2. Pokaż historię")
    print("3. Zapisz historię (CSV/XML)")
    print("4. Generuj wykres")
    print("0. Koniec")
    return input("Wybierz: ")

def uruchom():
    dystrybutory = {
        1: DystrybutorPaliwa(1,'ON',5000),
        2: DystrybutorPaliwa(2,'PB',3000)
    }
    historia = []
    while True:
        opcja = pokaz_menu()
        if opcja == '1':
            try:
                pid = int(input("ID dystrybutora: "))
                il = float(input("Litry: "))
                c = float(input("Cena za litr: "))
                tx = dystrybutory[pid].wydaj(il, c)
                print(">>", tx)
                historia.append(tx)
            except (ValueError, KeyError) as e:
                print("Błąd:", e)
            except BladDystrybutora as bd:
                print("Brak paliwa:", bd)
        elif opcja == '2':
            for t in historia: print(t)
            print("Śr. cena za litr:", srednia_cena(historia))
        elif opcja == '3':
            zapisz_do_csv(historia); zapisz_do_xml(historia)
            print("Zapisano.")
        elif opcja == '4':
            rysuj_wykres(historia); print("Wykres gotowy.")
        elif opcja == '0':
            break
        else:
            print("Nieznana opcja.")
