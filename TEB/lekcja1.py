tekst = """Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie."""

samogłoski = "aąeęiouóy"

tekst = tekst.lower()

counter = 0

for letter in tekst:
    if letter in samogłoski:
        counter += 1

print(counter)
