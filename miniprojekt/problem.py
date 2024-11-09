maile = []
końcówki = {'gmail' : "@gmail.com", 'wp': '@wp.pl' }
dane = {'imie' : 'Hubert', 'nazwisko' : "Rakowski"}
def dodaj_maila(imie, nazwisko, koniec):
    mail = f'{imie}.{nazwisko}{końcówki[koniec]}'
    maile.append(mail)
    print(mail)

dodaj_maila(dane['imie'], dane['nazwisko'], 'gmail')
dodaj_maila('Monika', 'Kowal', 'wp')
print(maile)

with open('maile.txt', "w") as file:
    for mail in maile:
        file.write(mail+'\n')

