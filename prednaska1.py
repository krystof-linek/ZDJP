
def prirazeni():
    a = b = c = 1

    print(a) # --> 1


"""
---- datove typy ----
- float()
- int()
- complex()
- bool()
- str()
- None

"""


def pretypovani():
    cislo = 5.5 # float
    print(int(cislo))

    # cislo = int("5a")
    # print(int(cislo)) --> vyhodí vyjimku


"""
pravda = True
nepravda = False
nic = None
"""


def stringy():
    vstup = input("Zadej neco: ") # vstup od uzivatele
    # delka stringu
    print(len(vstup))

    # escapovani
    print(r'C:\some\some')
    # nebo
    print('C:\\some\\some')

    # vypis promenne
    jmeno = "Mikulas"
    # nepouzivat
    # print('Ahoj', jmeno)
    # print('Ahoj' + jmeno)

    # pouzivat f string
    print(f"Ahoj {jmeno} {10+20}")
    # nasobeni stringu
    print(3 * "pra" + " babicka")


def indexovani():
    slovo = "Python"
    print(slovo[0]) # --> prvni znak
    print(slovo[-1]) # --> posledni znak
    # interval
    print(slovo[0:2]) # --> vypise Py
    print(slovo[-2:]) # vypise on


def multi_line_string():
    # multi line string
    text = """
        prvni radek
        druhy radek
        treti radek
    """
    print(text)

    # komentar multi line
    """

    tohle je muj komentar

    """

""" datove struktury """


def struktura_list():
    # list - seznam (implementovan jako dynamical array)
    l1 = [1, 2, 3]
    l2 = list()
    # l1[99] -> vyhodi vyjimku
    # pridani a odebrani
    l1.append(4)
    posledni = l1.pop()
    print(posledni)

    # scitani seznamu
    l3 = l1 + l2
    print(l3)
    # nasobeni
    l4 = (l1 * 5) + 12
    print(l4)


def referencovani():
    # referencovani
    L = [1, 2, 3]
    K = L
    K.pop()
    print(id(L)) # --> adresy budou stejne
    print(id(K))

    # muzu pouzit copy a zbavim se refencovani ==> dve mista v pameti
    A = 1
    B = A
    B = 5
    print(A) # --> vypise 1 = reference neni obousmerna

    C = 1
    D = 1
    print(id(C))
    print(id(D)) # --> stejne adresy

    # v pythonu se vzdycky vytavri nove objekty, na ty objekty pak ukazuji promenne


def fronta():
    # list jako fronta
    fronta = list()
    fronta.append("eva")
    fronta.append("tomas")
    print(fronta.pop(0)) # neni optimalni => je lepsi pouzi nejakou strukturu na frontu


def struktura_taple():
    t = (1, 2, 3)
    # taple nelze upravovat t[0] = 10 --> vyhodi vyjimku


def mnozina():
    # set - mnozina
    s = {'eva', 'tomas'} # --> nezalezi na poradi (muze se menit), neobsahuje duplicity
    # muzu provadet mnozinove operace
    # pridani a odebrani
    s.add('mikulas')
    s.discard('eva')
    # budou mnohem rychlejsi -> hledani v konstantim case udajne
    # muzu udelat frozen set --> nepujde pak upravit
    # taple a frozen set nikdo neupravi --> nikdo to pak omylem nepokazi


def ridici_konstrukce():
    """
     != nerovna se
     == rovna se --> porovnava shodnost obsahu
     is --> jestli se referencuje stejny objekt id1 == id2

    """

    # ruzne datove typy
    a = 1
    b = "1"
    print(a == b) # --> false

    # operator in --> jestli je neco v necem
    # "s" in "slon" --> true
    # 1 in [1, 2, 3] --> ano


def porovnani():
    cislo = 42
    if cislo > 10:
        print("Vetsi nez 10") # zalezi na odsazeni
    elif cislo < 0:
        print("Zaporne cislo")
    else:
        print("Ostatni pripady")


def cyklus_for():
    """
        for --> neni zde klasicky for --> musime vzdy skrz neco iterovat
    """
    zoo = ['pes', 'slon']

    for zvire in zoo:
        print(zvire.upper())

    # pokud chci klasicky

    for i in range(10, 51, 5): # od 10 do 50 po 5
        print(i)

    # pro vypis i poradi
    for i, zvire in enumerate(zoo):
        print(i, zvire)


def slovnik():
    # slovnik
    slovnik = {'mikulas': 156789657, 'eva': 345654123}
