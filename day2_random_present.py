import random

"""
     * Mikołaj postanowił w tym roku skorzystać z pomocy nowoczesnych technologii.
     * Zamiast zastanawiać się, komu jaki prezent dostarczyć postanowił skorzystać z programu.
     * Pomoż Mikołajowi!
     * Przygotuj kod, który z listy dostępnych prezentów wylosuje 3 prezenty i wypisze na ekranie.
     * Odpal program kilka razy - sprawdź, czy na pewno losuje za kazdym razem inne prezenty!
     * Wylosowane prezenty wypisz na ekranie. Zadbaj o to, żeby wylosowane prezenty były unikalne.
"""
ideas = ["Perfume", "Socks", "Sweater", "Cup",
         "Hat", "Tea", "Coffee", "Clock", "Bag",
         "Book", "Wallet", "Cream", "Earrings"]


def draw_ideas(how_many):
    ideas_poll = len(ideas)
    drawn_numbers = []
    while len(drawn_numbers) < how_many:
        draw = random.randrange(0, ideas_poll)
        if draw in drawn_numbers:
            continue
        drawn_numbers.append(draw)
    print(f"You have drawn the following {how_many} presents:")
    for i in drawn_numbers:
        print(ideas[i])
    print("Merry Christmas!")


#  Now draw three presents
draw_ideas(3)
