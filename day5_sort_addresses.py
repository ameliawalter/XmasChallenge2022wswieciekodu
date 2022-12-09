"""
* Pomóż Mikołajowi w rozwożeniu prezentów!
* Posortuj listę adresów dzieci po miastach alfabetycznie,
* tak, żeby Mikołaj mógł wygodnie zaplanować plan podrózy.
* Posortowaną listę adresów wypisz na ekranie.
* To bardzo proste zadanie! Więc dodatkowym plusem będzie
* wykonanie sortowania w jednej linijce. :D
"""
addresses = [["Swiateczna",
              "234",
              5,
              "Warszawa",
              "02-326"], ["Choinkowa",
                          "34A",
                          1,
                          "Krakow",
                          "31-326"], ["Mikolaja Swietego",
                                      "87",
                                      3,
                                      "Rzeszow",
                                      "40-326"], ["Bombkowa",
                                                  "214",
                                                  55,
                                                  "Gdansk",
                                                  "15-326"], ["Prezentowa",
                                                              "543",
                                                              765,
                                                              "Warszawa",
                                                              "02-326"], ["Serniczkowa",
                                                                          "4B",
                                                                          2,
                                                                          "Krakow",
                                                                          "02-326"], ["Pierniczkowa",
                                                                                      "289",
                                                                                      55,
                                                                                      "Gdansk",
                                                                                      "02-326"], ["Barszczykowa",
                                                                                                  "234",
                                                                                                  5,
                                                                                                  "Rzeszow",
                                                                                                  "37-326"],
             ["Uszkowa",
              "43H",
              5,
              "Wroclaw",
              "02-326"], ["Cukierkowa",
                          "23",
                          5,
                          "Poznan",
                          "02-326"]]

sorted_addresses = sorted(addresses, key=lambda x: x[3])
print(sorted_addresses)

