def get_gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def get_lcd(n, m):
    return n * m // get_gcd(n, m)

def solution(n, m): 
    return [get_gcd(n, m), get_lcd(n, m)]