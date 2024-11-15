<br />
<div align="center">
  <h3 align="center">Zadanie rekrutacyjne</h3>
</div>


## Zawartość
Projekt prostej aplikacji w języku Python w ramach zadania rekrutacyjnego dla firmy Oxido.
Zarówno zadanie podstawowe jak i dodatkowe zostało stworzone w dwóch wersjach: <br />
-Wersja opatrzona końcówką (kod) - skrypt do uruchomienia poprzez edycję kodu; <br />
-Wersja opatrzona końcówką (skrypt uruchamialny) - ten sam skrypt, zrefaktoryzowany pod kątem uruchamiania z poziomu wiersza poleceń

Aplikacja:
* Łączy się z API openAI
* Odczytuje treść artykułu z pliku tekstowego
* Przekazuje do OpenAI artykuł wraz z instrukcjami obróbki
* Przekierowuje odpowiedź do pliku HTML

### Wykorzystane technologie

* [![Python][Python]][Python-url]


## Uruchamianie
Oto przykład uruchomienia obu rodzai aplikacji:

### Zadanie podstawowe i dodatkowe - Wersja (kod)

W celu uruchomienia skryptu należy najpierw edytować go w dowolnym edytorze tekstu, aby wprowadzić swój klucz do API
* plik skrypt.py
  ```sh
  client = OpenAI(api_key="TU UMIEŚĆ KLUCZ API")
  ```
  po wykonaniu tej czynności aplikacja jest gotowa do kompilacji

### Zadanie podstawowe - wersja (skrypt uruchamialny)

aby uruchomić skrypt po pobraniu folderu z zawartością należy wprowadzić do niego zmienne z poziomu wiersza poleceń

1. Uruchom wiersz poleceń
2. Przejdź do folderu w którym znajduje się skrypt (poniżej przykład dla folderu znajdującego się na pulpicie użytkownika "user"
   ```sh
   C:\> cd Users/user/Desktop/"zadanie 1 - Python (skrypt uruchamialny)"
   ```
3. Uruchom plik podając jako argumenty najpierw swój klucz do API, a następnie ścieżkę do pliku, w którym znajduje się artykuł
   ```sh
   C:\Users\user\Desktop\zadanie 1 - Python (skrypt uruchamialny)> python skrypt.py TWOJ_KLUCZ_API SCIEZKA_DO_PLIKU_Z_ARTYKULEM
   ```
4. W przypadku problemów posłuż się komendą "python skrypt.py -h"
   ```sh
   >python skrypt.py -h
   ```
   ```
   usage: skrypt.py [-h] klucz_api artykul
   
   Skrypt do refaktoryzacji treści artykułu na kod HTML przy użyciu sztucznej inteligencji

   positional arguments:
     klucz_api  twój klucz API do połączenia z openAI API
     artykul    lokalizacja pliku zawierającego treść artykułu

   options:
     -h, --help  show this message and exit
   ```


### Zadanie dodatkowe - wersja (skrypt uruchamialny)

aby uruchomić skrypt po pobraniu folderu z zawartością należy wprowadzić do niego zmienne z poziomu wiersza poleceń

1. Uruchom wiersz poleceń
2. Przejdź do folderu w którym znajduje się skrypt (poniżej przykład dla folderu znajdującego się na pulpicie użytkownika "user"
   ```sh
   C:\> cd Users/user/Desktop/"zadanie dodatkowe - Python (skrypt uruchamialny)"
   ```
3. Uruchom plik podając jako argument swój klucz do API
   ```sh
   C:\Users\user\Desktop\zadanie dodatkowe - Python (skrypt uruchamialny)> python skrypt.py TWOJ_KLUCZ_API 
   ```
4. W przypadku problemów posłuż się komendą "python skrypt.py -h"
   ```sh
   >python skrypt.py -h
   ```
   ```
   usage: skrypt.py [-h] klucz_api 
   
   Skrypt do generowania szablonu artykułu w języku HTML

   positional arguments:
     klucz_api  twój klucz API do połączenia z openAI API

   options:
     -h, --help  show this message and exit
   ```
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
