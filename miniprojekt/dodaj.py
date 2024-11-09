końcówki = {'gmail' : "@gmail.com", 'wp': '@wp.pl' }
def dodaj_maila(imie, nazwisko, koniec, kolekcja: list):
    mail = f'{imie}.{nazwisko}{końcówki[koniec]}'
    kolekcja.append(mail)
    print(mail)