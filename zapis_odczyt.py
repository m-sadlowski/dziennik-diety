import json
from pathlib import Path
from datetime import datetime

from klasy import Dziennik, Pomiar

def zapisz_dziennik(dziennik: Dziennik, sciezka: str) -> None:

    dane = {
        "wzrost_m": dziennik.wzrost_m,
        "pomiary": [
            {
                "timestamp": pomiar.timestamp.isoformat(timespec="minutes"), # Pozbycie sie sekund przy enter dla daty!
                "waga_kg": pomiar.waga_kg,
                "bmi": pomiar.bmi,
            }
            for pomiar in dziennik.pomiary
        ],
    }
    path = Path(sciezka)
    with path.open("w", encoding= "utf-8") as f:
        json.dump(dane, f, indent=2)


def zaladuj_dziennik(sciezka: str) -> Dziennik:
    """
    Wczytywanie dziennika z pliku JSON + zwracanie nowego obiektu dziennik
    """
    path = Path(sciezka)
    if not path.exists():
        raise FileNotFoundError(f"Plik '{sciezka}' nie istnieje")
    with path.open("r", encoding = "utf-8") as f:
        dane = json.load(f)

    wzrost_m = dane["wzrost_m"]
    dziennik = Dziennik(wzrost_m=wzrost_m)

    for item in dane.get("pomiary", []):
        ts = datetime.fromisoformat(item["timestamp"]) #fromisoformat bo odczyt to string -> obiekt
        pomiar = Pomiar(
            timestamp=ts,
            waga_kg=item["waga_kg"],
            bmi=item["bmi"],
        )
        dziennik.pomiary.append(pomiar)
    return dziennik


