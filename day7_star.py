import turtle
"""
* Mikołaj postanowił w tym roku skorzytać z pomocy nowoczesnych technologii.
     * Zamiast kupować choinkę i ozdoby postanowił użyć takich wygenerowanych w konsoli
     * Pomoż Mikołajowi! Przygotuj kod, który wypisze na ekranie gwiazdkę.
     * Jeżeli potrafisz, nie wpisuj gwiazdki bezposrednio w printy - pokombinuj z pętlami.
     * Tak, żeby gwiazdka wygenerowała się sama!
     * Gwiazdka może mieć dowolny kształt, wygeneruj taki jaki potrafisz. Przykładowe gwiazdki:
     *     *       *       *         *
     *     *         *   *        *******
     * *********   **********      *****
     *     *         *   *        *******
     *     *       *       *         *
"""
screen = turtle.Screen()
turtle.title('Christmas star')
turtle.bgcolor('magenta')
turtle.pensize(10)
turtle.pencolor('yellow')
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()

screen.exitonclick()
