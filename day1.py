"""
 * Wyzwanie Świąteczne @wswieciekodu
 * Dzień 1
 * Mikołaj musi odwiedzić 3 miasta o współrzędnych (1,1), (4,5), (11,5) w podanej kolejności.
 * Mikołaj startuje z punktu(1,1) spod stacji paliw ;)
 * Na 10 jednostek odległości jego sanie zużywają 20 litrów magicznego paliwa.
 * Ile paliwa potrzebuje na całą trasę? Do policzenia przygotuj odpowiedni kod.
 * Obliczony wynik wypisz na ekranie.
"""
#  coordinates for the first city
xc1 = 1
yc1 = 1
#  coordinates for the second city
xc2 = 4
yc2 = 5
#  coordinates for the third city
xc3 = 11
yc3 = 5
# Euklides formula to calculate distance
def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


# Required flights and their sum to calculate itinerary
flight_1_to_2 = distance(xc1, yc1, xc2, yc2)
flight_2_to_3 = distance(xc2, yc2, xc3, yc3)
itinerary = int(flight_1_to_2 + flight_2_to_3)
print(f"Santa needs to travel the distance of {itinerary} units")

# Fuel usage: 20 l per 10 distance units, so 2 l per 1 unit
fuel_usage = int(itinerary * 2)
print(f"Santa needs to fill his tank with {fuel_usage} l of magic fuel")

