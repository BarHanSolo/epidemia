Projekt z Modelowania i symulacji komputerowej, zad 1 dotyczące symulacji epidemii w grupie 488 zwierząt.

1. Warunki brzegowe:

Zbuduj model symulacyjny epidemii w grupie 488 zwierząt przyjmując za podstawę umowny jednostkowy czas symulacji. Choroba rozwija się w dwóch etapach:

    a) Pierwszy bezobjawowy, zwierze jednak zaraża,

    b) Drugi objawowy, zwierze w dalszym ciągu zaraża.

Każdy etap trwa jednostkowy czas symulacji. Końcem choroby może być wyzdrowienie lub śmierć. Wyzdrowienie łączy się z czasową odpornością na ponowne zarażenie, która trwa również jednostkowy czas symulacji. Należy uwzględnić, że średnia długość życia zwierząt wynosi 6 umownych jednostek czasu z odchyleniem standardowym ±1 jednostka. Zwierzęta również się rozmnażają. Począwszy od wieku – dwie umowne jednostki czasu.

Należy założyć następujące wskaźniki przyrostu naturalnego:

- wiek: 2-4 u.j.c. 15±2%,

- wiek: 5-6 i więcej u.j.c. 10±1%.

Prawdopodobieństwo urodzenia chorego potomstwa jest wprost proporcjonalna do liczby chorych zwierząt w danej grupie wiekowej.

Liczebność zwierząt  zdrowych i chorych w poszczególnych grupach wiekowych prezentuje tabela.

| Wiek w u.j.c        | Liczba zwierząt zdrowych         | Liczba zwierząt chorych  |
| ------------- |:-------------:| -----:|
| 1      | 80 (20 czasowa odporność) | 20 (10 faza 1, 10 faza 2) |
| 2      | 90 (30 czasowa odporność)  |   30 (10 faza 1, 20 faza 2) |
| 3 | 80 (10 czasowa odporność)      |    15 (5 faza 1, 10 faza 2) |
| 4 | 70 (10 czasowa odporność)      |    15 (10 faza 1, 5 faza 2) |
| 5 | 40 (20 czasowa odporność)      |    10 (7 faza 1, 3 faza 2) |
| 6 | 15 (5 czasowa odporność)      |    10 (6 faza 1, 4 faza 2) |
| 7 | 10      |    3 ( 3 faza 2) |
 
Poziom śmiertelności zmienia się również wraz z wiekiem:

Zwierzęta młode (1-3 u.j.c.) 20±5%

Zwierzęta w średnim wieku (4-5 u.j.c.) 30±7%

Zwierzęta stare (6- u.j.c.) 50±15%.

2. Realizacja

Główna funkcja tworząca symulację ma 3 parametry. Pierwszym jest długość symulacji w standardowych jednostakch czasu. 

Warunki rozpisane w temacie zadania pozostawiają pole do interpretacji jak zwierzęta zarażają się między sobą. Dlatego warunki zarażania się zostały sparametryzowane za pomocą dwóch dodatkowych parametrów: contagiousness wyrażone w procentach oznacza jak bardzo zaraźliwa jest choroba (jaka jest procentowa szansa zarażenia się przy kontakcie) oraz contact oznaczające ilość zwierząt, z którymi dane zwierzę ma kontakt w jednostce czasu.

Na podstawie warunków początkowych wygenerowana została tablica zawierająca wszystkie zwierzęta. Każde zwierzę jest tuplem, którego wartości to:

1. wiek zwierzęcia w standardowych jednostkach czasu
2. status choroby (0 - zdrowy, 1 - odporny, 2 - etap objawowy, 3 - etap bezobjawowy, 4 - właśnie się zaraził)

Symulacja została podzielona na kilka etapów:

2.1. Funkcja infect

Z listy zwierząt wybiera losowo ilość zwierząt określoną w parametrze contact. Jeżeli wybrane zwierzę jest chore oraz funkcja random zwróci wartość mniejszą niż contagiousness dochodzi do zarażenia (status zwierzęcia zmienia się na 4).

2.2. Funkcja breed

Zwierzęta rozmnażają się zgodnie z parametrami określonymi w temacie zadania. Najpierw sprawdzany jest wiek rodzica, później funkcją random warunek na rozmnożenie się, a następnie za pomocą funkcji wyliczających ilośc chorych zwierząt w danej grupie wiekowej określane jest czy zwierzę urodzi się chore czy zdrowe.

2.3. Funkcja die

Podzielona na dwie części:

2.3.1. dieAge

Na podstawie odchylenia standardowego z tematu zadania wylicza prawdopodobieństwo śmierci zwierzęcia z powodu jego wieku. Jeżeli zwierzę umiera, to usuwa je z listy zwierząt.

2.3.2. dieIllness

Na podstawie odchylenia standardowego z tematu zadania wylicza prawdopodobieństwo śmierci zwierzęcia z powodu jego choroby. Jeżeli zwierzę umiera, to usuwa je z listy zwierząt.

2.4 Funkcja passTime

Odpowiada za zmianę współczynników z upłwającym czasem. Jest ostatnią funkcją jednostki symulacji. Po wykonaniu tej funkcji statusy zwierząt są już statusami z następnego okresu. Zwiększa wiek każdego zwierzęcia o 1 oraz obniża status choroby o 1 (chyba, że zwierzę jest zdrowe).

3. Wyniki

Każda symulacja została wykonana 100 razy dla każdych warunków. Średnia ilość żywych zwierząt na koniec zostaje zapisana do tabeli w pliku xml. Warunki sparametryzowane to zaraźliwość (5 do 20% co 5 procent) oraz ilość kontaktów z innymi zwierzętami w stadzie (od 0 do 25 kontaktów z innymi zwierzętami).
