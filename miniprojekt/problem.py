from dodaj import dodaj_maila
dane = {'imie' : 'Hubert', 'nazwisko' : "Rakowski"}
maile = []

dodaj_maila(dane['imie'], dane['nazwisko'], 'gmail', maile)
dodaj_maila('Monika', 'Kowal', 'wp', maile)

with open('maile.txt', "x") as file:
    file.writelines(maile)