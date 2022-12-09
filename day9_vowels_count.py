"""
* Mikołaj wykupił pakiet wysyłkowy do prezentów, ale przyoszczędził na wersji premium.
* Przez to będzie musiał dopłacić 2 zł za każdą samogłoskę w adresie.
* Pomóż Mikołajowi i policz ile będzie musiał dopłacić, a policzoną wartość wypisz na ekranie.
* Adresy znajdziesz w przygotowanej liście, nie ma w nich polskich znaków.
"""

addresses = [["Serniczkowa",
              "4B",
              2,
              "Krakow",
              "02-326"], ["Pierniczkowa",
                          "289A",
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
                                                  "02-326"], ["Cukierkowa",
                                                              "23I",
                                                              5,
                                                              "Poznan",
                                                              "02-326"]]

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
amount_to_pay = 0
# Flatten two-dimensional list of addresses:
flattened_list = []
for sublist in addresses:
    for i in sublist:
        flattened_list.append(i)
# Convert every element of the flattened list to a lowercase string:
strings_list = [str(x).lower() for x in flattened_list]
# Split every string into a list of chars and verify if a char is in vowels set,
# if so then increment amount to pay by 2:
for j in strings_list:
    chars = [c for c in j]
    for char in chars:
        if char in vowels:
            amount_to_pay += 2
        else:
            continue
# Print the result
print(f'Santa needs to pay {amount_to_pay} PLN')

