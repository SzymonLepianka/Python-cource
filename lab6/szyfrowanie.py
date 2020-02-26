import string

czyste_haslo = ""
szyfr_cezar = ""
deszyf_brutus=""
szyfr_przest=""
deszyf_przest=""


def czyste(haslo):
    global czyste_haslo
    for i in haslo:
        if i in string.ascii_letters:
            czyste_haslo += i
    czyste_haslo = czyste_haslo.lower()


def cezar(tekst, przesuniecie):
    global szyfr_cezar
    for i in tekst:
        for j in range(26):
            if i == string.ascii_lowercase[j]:
                if j + przesuniecie < 26:
                    print(string.ascii_lowercase[j + przesuniecie], end="")
                    szyfr_cezar+=string.ascii_lowercase[j + przesuniecie]
                else:
                    print(string.ascii_lowercase[j + przesuniecie - 26], end="")
                    szyfr_cezar+=string.ascii_lowercase[j + przesuniecie - 26]


def brutus(kod, przesuniecie):
    global deszyf_brutus
    for i in kod:
        for j in range(26):
            if i == string.ascii_lowercase[j]:
                if j - przesuniecie >= 0:
                    print(string.ascii_lowercase[j - przesuniecie], end="")
                    deszyf_brutus+=string.ascii_lowercase[j - przesuniecie]
                else:
                    print(string.ascii_lowercase[j - przesuniecie + 26], end="")
                    deszyf_brutus+=string.ascii_lowercase[j - przesuniecie + 26]

def podstawieniowy(tekst, alfabet):
    global szyfr_przest
    for i in tekst:
        for j in range(26):
            if i == string.ascii_lowercase[j]:
                print(alfabet[j],end="")
                szyfr_przest+=alfabet[j]

def dePodstawieniowy(kod, alfabet):
    global deszyf_przest
    for i in kod:
        for j in range(26):
            if i == alfabet[j]:
                print(string.ascii_lowercase[j], end="")
                deszyf_przest += string.ascii_lowercase[j]


haslo = input("podaj hasło: ")
przesuniecie = int(input("podaj przesuniecie: "))

czyste(haslo)
print(czyste_haslo)
cezar(czyste_haslo, przesuniecie)
print("")
print(szyfr_cezar)
brutus(szyfr_cezar,przesuniecie)
alfabet="1234567890qwertyuiopasdfgh"
print("")
podstawieniowy(czyste_haslo,alfabet)
print("")
dePodstawieniowy(szyfr_przest,alfabet)
