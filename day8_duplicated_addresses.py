"""
* Złośliwe chochliki poduplikowaly wpisy na liście adresów dzieci.
* Pomóż Mikołajowi i zdeduplikuj listę. Wypisz wyczyszczoną z duplikatów listę na ekran.
* Możesz usunąć niepotrzebne adresy z listy, albo utworzyć nową bez duplikatów.
"""

addresses = [["Serniczkowa",
              "4B",
              2,
              "Krakow",
              "02-326"], ["Pierniczkowa",
                          "289",
                          55,
                          "Gdansk",
                          "02-326"], ["Pierniczkowa",
                                      "289",
                                      55,
                                      "Gdansk",
                                      "02-326"], ["Pierniczkowa",
                                                  "289",
                                                  55,
                                                  "Gdansk",
                                                  "02-326"], ["Barszczykowa",
                                                              "234",
                                                              5,
                                                              "Rzeszow",
                                                              "37-326"], ["Uszkowa",
                                                                          "43H",
                                                                          5,
                                                                          "Wroclaw",
                                                                          "02-326"], ["Uszkowa",
                                                                                      "43H",
                                                                                      5,
                                                                                      "Wroclaw",
                                                                                      "02-326"], ["Uszkowa",
                                                                                                  "43H",
                                                                                                  5,
                                                                                                  "Wroclaw",
                                                                                                  "02-326"],
             ["Cukierkowa",
              "23",
              5,
              "Poznan",
              "02-326"]]

addresses_unique = []
for i in addresses:
    if i not in addresses_unique:
        addresses_unique.append(i)
print(addresses_unique)
print(len(addresses_unique))
# Alternative solution - convert nested lists to tuples, then convert list of tuples to set to remove the duplicates
# list_to_set = set(tuple(i) for i in addresses)
# addresses_unique = [list(tup) for tup in list_to_set]
# print(addresses_unique)
# print(len(addresses_unique))

