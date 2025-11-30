from dataclasses import dataclass
from datetime import datetime
from typing import List

from narzedzia import bmi_oblicz

@dataclass
class Pomiar:
    """
    Pojedynczy pomiar wagi
    Atrybuty:
        timestamp: Data i godzina pomiaru
        waga_kg: waga w kilogramach
        bmi: Wartosc BMI liczona na podstawie wartosci wzrostu i wagi
    """
    timestamp: datetime
    waga_kg: float
    bmi: float

class Dziennik:
    """
    Dziennik pomiarow dla jendej osoby - o stałym wzroscie!!
    Przechowuje liste pomiarow wagi z datami
    pozwala dodawac pomiary, filtrowac po zakresie
    dat i poprawnosci wspolczynnika BMI
    """
    def __init__(self, wzrost_m) -> None:
        """
        Inincjalizacja Dziennika; nowy dziennik dla osoby o danym wzroscie
        :param wzrost_m: wzrost w metrach
        """
        self.wzrost_m: float = wzrost_m
        self.pomiary: List[Pomiar] = []

    def dodaj_pomiar(self, waga_kg: float, timestamp: datetime | None = None) -> Pomiar:
        """
        Dodaje nowy pomiar wagi do dziennika
        Jezeli data i czas nie sa podane uzywamy aktualnej
        :param waga_kg: waga w kilogramach
        :param timestamp: data i godzina pomiaru/ None dla "teraz"
        :return: Obiekt pomiaru reprezentujacy nowy zapis w dzienniku
        """
        if timestamp is None:
            timestamp = datetime.now()
        bmi = bmi_oblicz(waga_kg, self.wzrost_m)
        pomiar = Pomiar(timestamp = timestamp, waga_kg = waga_kg, bmi = bmi)
        self.pomiary.append(pomiar)
        return pomiar
    ## dany okres dat (poczatek-koniec)
    def pomiar_okres(self, poczatek: datetime, koniec: datetime) -> List[Pomiar]:
        """
        Zwraca liste pomiarow z podanego zakresu czasu włacznie
        :param poczatek: poczatek zakresu (data i godzina)
        :param koniec: koniec (data i godzina)
        :return: Lista pomiarow dla ktorych timestamp zawiera sie w zakresie
        """
        return [p for p in self.pomiary if poczatek <= p.timestamp <= koniec]
    ##def pomiaru poza zakresem prawidlowego bmi
    def pomiar_nieprawidlowy(self, normal_min: float = 18.5, normal_max: float = 24.9) -> List[Pomiar]:
        """
        Zwara pomiary z wsp. BMI poza ustalonym zakresem normy
        :param normal_min: dolna granica zakresu normy
        :param normal_max: gorna granica zakresu normy
        :return: Lista pomiarow dla ktorych wartosci wspolczynnika BMI jest < normal_min i > normal_max
        """
        return [p for p in self.pomiary if p.bmi < normal_min or p.bmi > normal_max]