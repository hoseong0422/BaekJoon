def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcd(a, b):
    return a * b // get_gcd(a, b)

a, b = map(int, input().split())
print(get_gcd(a, b), get_lcd(a, b), sep='\n')