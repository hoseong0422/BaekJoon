def get_gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def get_lcd(n, m):
    return n * m // get_gcd(n, m)

a, b = map(int, input().split())
print(get_gcd(a, b), get_lcd(a, b), sep='\n')