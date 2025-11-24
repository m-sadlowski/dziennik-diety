from datetime import datetime, date

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

def parsowanie_daty(data_str: str) -> date:
    for format in ("%d.%m.%Y"):
        return datetime.strptime(data_str, format).date()

## formatowanie wyswietlnaych danych
def formatuj_pomiar(pomiar) -> str:
    stempel = pomiar.timestamp.strftime("%d.%m.%Y")
    return f"{stempel} | {pomiar.waga_kg:.1f} kg | BMI: {pomiar.bmi:.2f}"