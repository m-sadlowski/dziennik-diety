from dataclasses import dataclass
from datetime import datetime
from typing import List

from narzedzia import bmi_oblicz

@dataclass
class Pomiar:
    timestamp: datetime
    waga_kg: float
    bmi: float

class Dziennik:

    def __init__(self, wzrost_m) -> None:
        self.wzrost_m: float = wzrost_m
        self.pomiary: List[Pomiar] = []

    def dodaj_pomiar(self, waga_kg: float, timestamp: datetime | None = None) -> Pomiar:
        if timestamp is None:
            timestamp = datetime.now()
        bmi = bmi_oblicz(waga_kg, self.wzrost_m)
        pomiar = Pomiar(timestamp = timestamp, waga_kg = waga_kg, bmi = bmi)
        self.pomiary.append(pomiar)
        return pomiar
    ## dany okres dat (poczatek-koniec)
    def pomiar_okres(self, poczatek: datetime, koniec: datetime) -> List[Pomiar]:
        return [p for p in self.pomiary if poczatek <= p.timestamp <= koniec]
    ##def pomiaru poza zakresem prawidlowego bmi
    def pomiar_nieprawidlowy(self, normal_min: float = 18.5, normal_max: float = 24.9) -> List[Pomiar]:
        return [p for p in self.pomiary if p.bmi < normal_min or p.bmi > normal_max]