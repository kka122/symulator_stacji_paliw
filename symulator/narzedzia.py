def silnia(n: int) -> int:
    assert n >= 0, "n ≥ 0"
    return 1 if n < 2 else n * silnia(n-1)

def loguj(funkcja):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {funkcja.__name__} args={args}, kwargs={kwargs}")
        return funkcja(*args, **kwargs)
    return wrapper

def filtruj_duze(transakcje, prog: float):
    return list(filter(lambda t: t.cena_calkowita >= prog, transakcje))
