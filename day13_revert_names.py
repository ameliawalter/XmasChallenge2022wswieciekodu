"""
     * Chochliki nie ułatwiają życia Mikołajowi. Tym razem poodwracały imiona dzieci na liście…
     * Napraw co popsuły chochliki i odwróć imiona.
     * Zwróć uwagę na duże litery i zamień je, tak, żeby imiona były poprawne.
     * Na koniec wypisz listę w terminalu żeby sprawdzić, czy wszystko jest ok!
"""
names = ["Uisaj", "Aisak", "Aisa", "Kemot", "Lahcim"]


def revert_names(names_list):
    reverted_names_list = []
    for name in names_list:
        reverted_names_list.append(name[::-1].capitalize())
    print(reverted_names_list)


revert_names(names)
