# zadanie 1. kody pocztowe
def kod_pocztowy(kod_poczatkowy,kod_koncowy):
    kod_poczatkowy.replace('-','')
    kod = int(kod_poczatkowy.replace('-',''))
    kod_petla = int(kod_koncowy.replace('-',''))
    while kod < kod_petla+1:
        nowy_kod = str(kod)
        print(nowy_kod[0]+nowy_kod[1]+"-"+nowy_kod[2]+nowy_kod[3]+nowy_kod[4])
        kod = kod+1

kod_pocztowy("79-900","80-155")


input("Wciśnij Enter aby przejść do Zadania 2")
### zadanie 2. listy

def listy(n):
    wejscie = [2,3,7,4,9],10
    wyjscie = [1,5,6,8,10]
    wejscie_po_obrobce = list(wejscie[0])
    wejscie_po_obrobce.append(wejscie[1])

    lista = []
    for i in range(1,n+1):
        lista.append(i)

    lista_wejscie = list.copy(lista)
    lista_wyjscie = list.copy(lista)

    for i in wyjscie:
        lista_wyjscie.remove(i)

    for i in wejscie_po_obrobce:
        lista_wejscie.remove(i)

    
    print("brakujące elementy na wyjsciu to: ", end="")
    print(lista_wyjscie)
    
    print("brakujące elementy na wejsciu to: ", end="")
    print(lista_wejscie)

listy(10)


input("Wciśnij Enter aby przejść do Zadania 3")
### zadanie 3. licznik


def odliczanie(l_pocz,l_konc):
    liczba = l_pocz-0.5
    while liczba < l_konc:
        liczba = liczba+0.5
        print(liczba)

odliczanie(2,5.5)
