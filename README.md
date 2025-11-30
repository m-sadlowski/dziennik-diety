# ismed2025Z_Sadlowski
# Dziennik przebiegu diety
Program w terminalu do zapisywania pomiarow wagi,
obliczania wspolczynnika BMI i zapisywania/odczytywania danych do/z pliku JSON

## Wymagania
- Python 3.10+
- nie ma potrzeby instalowania dodatkowych pakietow

## Jak uruchomic
1. Pobierz(zip) lub sklonuj git'em projekt
2. Otworz **powershell** albo **cmd**
3. Przejdz do odpowiedniego katalogu z projektem
4. wpisz **python main.py**

## Funkcjonalnosc

Program umozliwia:

- wprowadzenie **wzrostu uzytkownika** (w metrach),
- dodawanie pomiarów wagi z dokladnym **terminem wykonania**:
  - data (`DD.MM.RRRR`) i godzina (`HH:MM`)
  - lub użycie aktualnej daty
- automatyczne wyliczanie wspolczynnika **BMI**,
- tekstową ocenę BMI (niedowaga / norma / nadwaga / otylosc),
- wyswietlenie:
  - wszystkich pomiarów,
  - pomiarow z wybranego **okresu czasu**,
  - pomiarow z **BMI poza normą**,
- zapis i odczyt danych do/z pliku **JSON**.

## Struktura projektu

```text
dziennik-diety/
├── main.py          # glowny plik uruchomieniowy 
├── klasy.py         # definicje klas Pomiar i Dziennik
├── narzedzia.py     # funkcje pomocnicze (BMI, parsowanie daty, formatowanie)
├── zapis_odczyt.py  # zapis i odczyt dziennika do/z pliku JSON
├── README.md        # informacje
├── requirements.txt # informacje o zaleznosciach
└── to_do.md         # notatki / lista zadań