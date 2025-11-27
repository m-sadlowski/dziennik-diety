from klasy import Dziennik
from narzedzia import parsowanie_daty_godziny, formatuj_pomiar, ocena_bmi

def main() -> None:
    print("-- Test dziennika nr 2--")

    wzrost_str = input("Podaj wzrost w metrach (z kropka): ")
    wzrost = float(wzrost_str.replace(" ", ""))
    dziennik = Dziennik(wzrost_m = wzrost)

    waga_str = input("Podaj waga w kilogramach (z kropka): ")
    waga = float(waga_str.replace(" ", ""))


    data_str = input("Podaj date pomiaru wagi(dd.mm.rr)/ dzisiejsza = Enter").strip()
    if data_str:
        godzina_str = input("Podaj godzine pomiaru(hh:mm): ").strip()
        data_pomiaru = parsowanie_daty_godziny(data_str, godzina_str)
        pomiar = dziennik.dodaj_pomiar(waga_kg = waga, timestamp = data_pomiaru)
    else:
        pomiar = dziennik.dodaj_pomiar(waga_kg = waga)

    print()
    print("Zapisany pomiar: ")
    print(formatuj_pomiar(pomiar))
    print(ocena_bmi(pomiar.bmi))

if __name__ == "__main__":
    main()
