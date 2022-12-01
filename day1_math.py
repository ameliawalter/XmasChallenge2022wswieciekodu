import math
"""
 * Wyzwanie Świąteczne @wswieciekodu
 * Dzień 1
 * Mikołaj musi odwiedzić 3 miasta o współrzędnych (1,1), (4,5), (11,5) w podanej kolejności.
 * Mikołaj startuje z punktu(1,1) spod stacji paliw ;)
 * Na 10 jednostek odległości jego sanie zużywają 20 litrów magicznego paliwa.
 * Ile paliwa potrzebuje na całą trasę? Do policzenia przygotuj odpowiedni kod.
 * Obliczony wynik wypisz na ekranie.
"""
coords1 = (1, 1)
coords2 = (4, 5)
coords3 = (11, 5)

itinerary = int(math.dist(coords1, coords2) + math.dist(coords2, coords3))
print(f"Santa needs to travel the distance of {itinerary} units")

# Fuel usage: 20 l per 10 distance units, so 2 l per 1 unit
fuel_usage = int(itinerary * 2)
print(f"Santa needs to fill his tank with {fuel_usage} l of magic fuel")
