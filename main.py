from klasy import Dziennik
from narzedzia import parsowanie_daty_godziny, formatuj_pomiar, ocena_bmi

def dodaj_pomiar(dziennik: Dziennik) -> None:
    """ Pobieranie danych od uzytkownika dziennika i dodanie nowego pomiaru"""
    waga_str = input("Podaj waga w kilogramach (z kropka): ")
    waga = float(waga_str.replace(" ", ""))
    data_str = input("Podaj date pomiaru wagi(dd.mm.rr)/ dzisiejsza = Enter").strip()
    if data_str:
        godzina_str = input("Podaj godzine pomiaru(hh:mm): ").strip()
        data_pomiaru = parsowanie_daty_godziny(data_str, godzina_str)
        pomiar = dziennik.dodaj_pomiar(waga_kg = waga, timestamp = data_pomiaru)
    else:
        pomiar = dziennik.dodaj_pomiar(waga_kg = waga)

    print("Dodano pomiar: ")
    print(formatuj_pomiar(pomiar))
    print(ocena_bmi(pomiar.bmi))

def pokaz_pomiary(dziennik: Dziennik) -> None:
    """Wyswietlanie wszystkich pomiarow dziennika"""
    if not dziennik.pomiary:
        print("Brak pomiarow - najpierw dodaj jakis pomiar")
        return
    print("Wszystkie pomiary:")
    for pomiar in dziennik.pomiary:
        print(formatuj_pomiar(pomiar))

def pokaz_z_zakresu(dziennik: Dziennik) -> None:
    """Wyswietla pomiary z wybranego zakresu dat i godzin"""
    if not dziennik.pomiary:
        print("Brak pomiarow")
        return
    print("Podaj zakres czasu: ")
    data_start = input("Data poczatkowa: ").strip()
    godzina_start = input("Podaj godzine poczatkowa: ").strip()
    data_koniec = input("Data koniec: ").strip()
    godzina_koniec = input("Godzine koniec: ").strip()

    start = parsowanie_daty_godziny(data_start, godzina_start)
    koniec = parsowanie_daty_godziny(data_koniec, godzina_koniec)
    pomiary = dziennik.pomiar_okres(start, koniec)
    if not pomiary:
        print("Brak pomiarow w zakresie")
        return
    print("Pomiary z wybranego zakresu: ")
    for pomiar in pomiary:
        print(formatuj_pomiar(pomiar))

def pomiar_nieprawidlowe_bmi(dziennik: Dziennik) -> None:
    """Pomiary z BMI poza norma"""
    if not dziennik.pomiary:
        print("Brak pomiarow")
        return
    pomiary = dziennik.pomiar_nieprawidlowy()

    if not pomiary:
        print("Brak pomiarow z BMI poza norma")
        return
    print("Pomiary z BMI poza norma: ")
    for pomiar in pomiary:
        print(formatuj_pomiar(pomiar))
        print(" ", ocena_bmi(pomiar.bmi))

def wyswietl_menu() -> None:
    print("\n Dziennik przebiegu diety ")
    print("1. Dodaj nowy pomiar")
    print("2. Wyswietl wszystkie zapisane pomiary")
    print("3. Wyswietl pomiary z zapisanego okresu")
    print("4. Wyswietl pomiary z nieprawidlowym BMI")
    print("0. Zakoncz")


def main() -> None:
    print("-- Test dziennika nr 3 ; menu! --")

    wzrost_str = input("Podaj wzrost w metrach (z kropka): ")
    wzrost = float(wzrost_str.replace(" ", ""))
    dziennik = Dziennik(wzrost_m = wzrost)

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcje: ").strip()

        if wybor == "1":
            dodaj_pomiar(dziennik)
        elif wybor == "2":
            pokaz_pomiary(dziennik)
        elif wybor == "3":
            pokaz_z_zakresu(dziennik)
        elif wybor == "4":
            pomiar_nieprawidlowe_bmi(dziennik)
        elif wybor == "0":
            print("Koniec programu")
            break
        else:
            print("Zle - sproboj ponownie")

#    waga_str = input("Podaj waga w kilogramach (z kropka): ")
#    waga = float(waga_str.replace(" ", ""))
#
#
#   data_str = input("Podaj date pomiaru wagi(dd.mm.rr)/ dzisiejsza = Enter").strip()
#    if data_str:
#       godzina_str = input("Podaj godzine pomiaru(hh:mm): ").strip()
#        data_pomiaru = parsowanie_daty_godziny(data_str, godzina_str)
#        pomiar = dziennik.dodaj_pomiar(waga_kg = waga, timestamp = data_pomiaru)
#    else:
#        pomiar = dziennik.dodaj_pomiar(waga_kg = waga)
#
#    print()
#    print("Zapisany pomiar: ")
#    print(formatuj_pomiar(pomiar))
#    print(ocena_bmi(pomiar.bmi))

if __name__ == "__main__":
    main()
