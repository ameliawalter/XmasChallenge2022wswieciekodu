"""
* Pomóż Mikołajowi przygotować etykiety do druku na prezenty!
* Dla każdego dziecka z listy wypisz w konsoli imię, nazwisko i adres w formacie jak na list.
* Rozdziel przygotowane etykiety liniami.
"""
children_addresses = [("Jasiu",
                       "Kowalski", ("Serniczkowa",
                                    "4B",
                                    2,
                                    "Krakow",
                                    "02-326")), ("Kasia",
                                                 "Nowak", ("Pierniczkowa",
                                                           "289",
                                                           55,
                                                           "Gdansk",
                                                           "02-326")), ("Asia",
                                                                        "Wisniewska", ("Barszczykowa",
                                                                                       "234",
                                                                                       5,
                                                                                       "Rzeszow",
                                                                                       "37-326")), ("Tomek",
                                                                                                    "Wojcik",
                                                                                                    ("Uszkowa",
                                                                                                     "43H",
                                                                                                     5,
                                                                                                     "Wroclaw",

                                                                                                     "02-326"))]



address_fields = []
for i in children_addresses:
    for j in i[2:]:
        address_fields.append(j)

for address in children_addresses:
    for field in address_fields:
        if field in address:
            print(address[0], address[1])
            print(field[0], field[1], '/', str(field[2]), '\n', field[3], field[4], '\n', '-', '\n')





