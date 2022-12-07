"""
 * Mikołaj postanowił w tym roku skorzytać z pomocy nowoczesnych technologii.
     * Zamiast kupować choinkę i ozdoby postanowił użyć takich wygenerowanych w konsoli (terminalu)
     * Pomoż Mikołajowi! Przygotuj kod, który wypisze na ekranie choinkę.
     * Jeżeli potrafisz, nie wpisuj drzewka bezposrednio w printy - pokombinuj z pętlami.
     * Przygotuj funkcję przyjmującą wysokość choinki i wypisującą choinkę na ekranie.
     * Tak, żeby choinka wygenerowała się sama! Choinka może być po prostu trójkątem, albo być żłożona z kilku warstw. :)
"""

def print_christmas_tree():
    n = int(input('What tree size would you like? Pick a number between 3 for extra small and 30 for extra large: '))
    tree_block = '*'
    s = ' '
    #  n = 10
    base_length = 2 * n
    while len(tree_block) < base_length:
        print(n * s, tree_block, n * s)
        tree_block += '**'
        n -= 1
    print('Merry Xmas!')


print_christmas_tree()
