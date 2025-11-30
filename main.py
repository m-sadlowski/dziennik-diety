from klasy import Dziennik
from narzedzia import parsowanie_daty_godziny, formatuj_pomiar, ocena_bmi
from zapis_odczyt import zapisz_dziennik, zaladuj_dziennik

def dodaj_pomiar(dziennik: Dziennik) -> None:
    """
    Dodaje nowy pomiar wagi na postawie danych wpisanych przez uzytkownika
    Funkcja pobiera z klawiatury wage i opcjonalnie data + godzina pomiaru
    w przypadku nie podania daty(enter) uzywana jest aktualna data i czas
    Nowy pomiar jest zapisywany w obiekcie dziennik a sam wynik wypisywany
    jest rowniez w terminalu(waga, BMI i jego ocena)
    :param dziennik: obiekt Dziennik, do ktorego ma zostac przekazany pomiar
    """
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
    """
    Wyswietla wszystkie pomiary zapisane w dzienniku
    Jezeli w dzienniku nie ma pomiarow, wypisywana jest informacja
    o braku pomiarow; powrot do menu
    :param dziennik: obiekt Dziennik z lista pomiarow
    """
    if not dziennik.pomiary:
        print("Brak pomiarow - najpierw dodaj jakis pomiar")
        return
    print("Wszystkie pomiary:")
    for pomiar in dziennik.pomiary:
        print(formatuj_pomiar(pomiar))

def pokaz_z_zakresu(dziennik: Dziennik) -> None:
    """
    Wyswietlanie pomiarow z wybranego przez uzytkownika zakresu czasu

    Pytanie o date i godzine poczatkowa oraz koncowa a nastepnie
    wykorzystanie metody pomiar_okres z klasy Dziennik'a do
    odfiltrowania odpowiednich wpisow
    :param dziennik: obiekt Dziennik z ktorego maja zostac pobrane pomiary
    """
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
    """
    Wyswietla wszystkie pomiary dla ktorych
    wspolczynnik BMI jest poza norma
    Zakres przyjety to 18.5 - 24.9. Funkcja korzysta
    z metody pomiar_nieprawidlowy klasy Dziennik a nastepnie
    wypisuje kazdy nieprawidlowy pomiar wraz z ocena tekstowa
    :param dziennik: obiekt Dziennik z lista pomiarow
    """
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
    """
    Wypisuje w terminalu glowne menu
    """
    print("\n Dziennik przebiegu diety ")
    print("1. Dodaj nowy pomiar")
    print("2. Wyswietl wszystkie zapisane pomiary")
    print("3. Wyswietl pomiary z zapisanego okresu")
    print("4. Wyswietl pomiary z nieprawidlowym BMI")
    print("5. Otworz dziennik z pliku")
    print("6. Zapisz dziennik do pliku")
    print("0. Zakoncz")


def main() -> None:
    """
    Glowna funkcja uruchamiajaca program dziennika diety
    """
    print("-- Dziennik diety --")

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
        elif wybor == "5":
            nazwa = input("Podaj nazwe pliku do wczytania(json): ").strip()
            if not nazwa:
                print("Nie podano nazwy")
            else:
                try:
                    dziennik = zaladuj_dziennik(nazwa)
                    print(f"Wczytano dziennik z pliku '{nazwa}'")
                except FileNotFoundError:
                    print("Taki plik nie istnieje")
        elif wybor == "6":
            nazwa = input("Podaj nazwe pliku do zapisu(json): ").strip()
            if not nazwa:
                print("Nie podano nazwy")
            else:
                try:
                    zapisz_dziennik(dziennik, nazwa)
                    print(f"Dziennik zapisany do pliku '{nazwa}'")
                except FileNotFoundError:
                    print("Taki plik nie istnieje")
        elif wybor == "0":
            print("Koniec programu")
            break
        else:
            print("Zle - sproboj ponownie")


if __name__ == "__main__":
    main()
