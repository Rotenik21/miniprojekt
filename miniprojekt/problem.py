maile = []
końcówki = {'gmail' : "@gmail.com", 'wp': '@wp.pl' }
dane = {'imiona' : 'Hubert', 'nazwiska' : "Rakowski"}
def dodaj_maila(imie, nazwisko, koniec):
    mail = f'{imie}.{nazwisko}{końcówki[koniec]}'
    maile.append(mail)
    print(mail)
dodaj_maila(dane['imie'], dane['nazwisko'], 'gmail')
