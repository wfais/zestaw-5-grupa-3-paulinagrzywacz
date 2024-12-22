from itertools import product



def maximize_expression(K, M, lists):
    wynik = 0
    for lista in product(*lists):
        liczba = sum(x**2 for x in lista) % M
        wynik = max(wynik, liczba)
        
    return wynik 


if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
