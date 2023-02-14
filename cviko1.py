
def task1():
    """
    1. priklad
    Vytvorte program, ktery bude generovat jmena tymu na zaklade jmen členu tymu.
    Jmeno tymu se vytvori spojenim prvnich dvou pismen členu tymu.

    """
    tym = ['eva', 'pepa', 'franta']

    nazev = ""

    for jmeno in tym:
        nazev += jmeno[:2]

    print(nazev)


def task2():
    """
    2. priklad
    Nactete od uzivatele vstup a vypiste jen jeho posledni polovinu

    """

    vstup = input()

    pocet = len(vstup)
    pocet = pocet // 2

    print(vstup[-pocet:])


def task3():
    """
    3. priklad

    Aproximujte hodnotu cisla pi pomoci nasledujiciho nekonecneho souctu
    pi^2/6 = 1/1 + 1/2^2 + 1/3^2 + 1/4^2 .....

    (mozna chyba v zadani)

    """

    soucet = 0
    for n in range(1, 10000):
        soucet += n ** -1

    print((soucet * 6)**0.5)

    # neni dodelano


def task4():
    """
    4. priklad

    Vytvorte program na generovani fibonaciho posloupnosti. Uzivatel zada, kolik clenu se ma vygenerovat a program vypise
    list obsahujici fib. posloupnost

    [0, 1]
    [0, 1, 1]
    [0, 1, 1, 2]

    """

    kolik = input()
    kolik = int(kolik)

    fib = [0, 1]
    for n in range(kolik):
        fib.append(fib[-1]+fib[-2])

    print(fib)


def task5():
    """
    5. priklad

    Naprogramujte hru kamen, nuzky, papir s pomoci modulu random. Uzivatel si zvoli moznost, pak si vybere stroj pomoci
    modulu random a nakonec vypise kdo vyhral.

    """
    from random import choice

    vitez = False

    while not vitez:
        hrac = input()
        stroj = choice(["kamen", "nuzky", "papir"])

        if hrac != stroj:
            vitez = True
            if hrac == "kamen" and stroj == "nuzky" or \
                    hrac == "nuzky" and stroj == "papir" or \
                        hrac == "papir" and stroj == "kamen":
                print(f" Hrac: {hrac} - Stroj: {stroj} ==> vyhrava hrac!")
            else:
                print(f" Hrac: {hrac} - Stroj: {stroj} ==> vyhrava stroj!")
        else:
            print(f" Hrac: {hrac} - Stroj: {stroj} ==> remiza!")


def task6():
    """
    6. priklad

    Vygenerujte pomoci operatoru nad stringy posldni sloku pisnicky
    Justin Bieber: Boyfriend, která zní:

    na na na, na na na, na na na ey
    na na na, na na na, na na na ey
    na na na, na na na, na na na ey
    na na na, na na na, na na na ey

    """

    print(4 * ((3 * (2 * "na " + "na, ")) + "ey\n"))


def task7():
    """
    7. priklad

    Mejme ulozena data o studentech jedna se o list listu.

    Kazdy prvek vnejsiho listu reprezentuje studenta.
    Vnitrni prvek obsahuje na prvni pozici jmeno studenta a na druhe pozici pocet ziskanych bodu. Predpokladejme, ze je
    venjsi list seřazen dle poctu ziskanych bodu.

    studenti = [ ["Roman", 95], ["Stepan", 70], ["Mikulas", 50] ]

    TASK1 - Vypiste jmeno studneta, který získal nejvice bodu
    TASK2 - Vypiste kolik bodu ziskal student s nejhorsim vysledkem
    """

    studenti = [ ["Roman", 95], ["Stepan", 70], ["Mikulas", 50] ]

    print(f"Nejvice bodu ziskal: {studenti[0][0]}")
    print(f"Nejmene bodu bylo: {studenti[-1][1]}")


def task8():
    """
    Prace se slovnikem

    key -> value

    """

    slovnik = {'mikulas': 156789657, 'eva': 345654123}

    print(slovnik.keys())
    print(slovnik.values())

    for jmeno, cislo in slovnik.items():
        print(f"{jmeno} ma cislo {cislo}")

# volani tasku

#task1()
#task2()
#task3() -> neni spravne
#task4()
task5()
#task6()
#task7()
#task8()
