from datetime import datetime

def bmi_oblicz(waga_kg: float, wzrost_m: float) -> float:
    """
    Oblicza wartość współczynnika BMI

    :param waga_kg:  Waga w kilogramach
    :param wzrost_m: Wzrost w metrach
    :return: BMI zaokrąglone do dwóch miejsc po przecinku
    :raises: ValueError: Gdy waga lub wzrost sa mniejsze/rowne zero
    """
    if waga_kg <= 0:
        raise ValueError("waga_kg <= 0; Waga musi byc wieksza od zera!")
    if wzrost_m <= 0:
        raise ValueError("wzrost_m <=0; Wzrost musi byc wiekszy od zera!")

    return round(waga_kg / (wzrost_m ** 2), 2)

def ocena_bmi(bmi: float) -> str:
    """
    Zwraca opisowa ocene BMI
    Skala: <18.5 - niedowaga
            18.5-24.9 - norma
            25.0-29.9 - nadwaga
            >= 30.0 - otylosc
    :param bmi: wartosc wspolczynnika bmi
    :returns: krotki opis kategorii bmi
    """
    if bmi < 18.5:
        return "BMI ponizej normy"
    elif bmi <= 24.9:
        return "BMI w normie"
    elif bmi <= 29.9:
        return "BMI powyzej normy"
    else:
        return "BMI znacznie powyzej normy"

def parsowanie_daty_godziny(data_str: str, godzina_str: str) -> datetime:
    """
    Zamiana tekstowej daty + godziny na obiekt datetime
    format:
        data_str -> 'DD.MM.YYYY', '20.09.2003'
        godzina_str -> 'HH:MM', '22:22'
    :param data_str: tekstowa data w formacie
    :param godzina_str: tekstowa godzina w formacie
    :return: obiekt datetime odpowiadjaacy podanej dacie i godzinie
    """
    tekst = f"{data_str} {godzina_str}"
    return datetime.strptime(tekst, "%d.%m.%Y %H:%M")

def formatuj_pomiar(pomiar) -> str:
    """
    Dane zostaja zamkniete w stempel i wyswietlone
    format:
        'DD.MM.YYYY' | XX.X kg | BMI: XX.XX'
    :param pomiar: obiekt pomiar do sformatowania
    :return: gotowy string z data, waga i BMI
    """
    stempel = pomiar.timestamp.strftime("%d.%m.%Y %H:%M")
    return f"{stempel} | {pomiar.waga_kg:.1f} kg | BMI: {pomiar.bmi:.2f}"