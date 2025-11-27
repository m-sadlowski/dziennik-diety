from datetime import datetime

def bmi_oblicz(waga_kg: float, wzrost_m: float) -> float:
    ## dodaj warunki wzrost,waga < 0 ; nie moza podac ujemnej wartosci
   return round(waga_kg / (wzrost_m**2), 2)

def ocena_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "BMI ponizej normy"
    elif bmi >18.5 and bmi < 24.9:
        return "BMI w normie"
    elif bmi > 24.9:
        return "BMI powyzej normy"

def parsowanie_daty_godziny(data_str: str, godzina_str: str) -> datetime:
    """
    Zamiana tekstowej daty + godziny na obiekt datetime
    data_str : np. '20.09.2003'
    godzina_st : np. '20:20'
    from narzedzia import xxx => help(xxx)!!!
    """
    tekst = f"{data_str} {godzina_str}"
    return datetime.strptime(tekst, "%d.%m.%Y %H:%M")

## formatowanie wyswietlnaych danych
def formatuj_pomiar(pomiar) -> str:
    """
    Dane zostaja zamkniete w stempel i wyswietlone ; test docstring
    """
    stempel = pomiar.timestamp.strftime("%d.%m.%Y %H:%M")
    return f"{stempel} | {pomiar.waga_kg:.1f} kg | BMI: {pomiar.bmi:.2f}"