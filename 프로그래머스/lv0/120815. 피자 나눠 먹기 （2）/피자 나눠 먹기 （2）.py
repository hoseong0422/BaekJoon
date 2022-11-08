def solution(n):
    # x * 6 % n = 0
    pizza = 1
    while True:
        if (pizza * 6) % n == 0:
            return pizza
        pizza += 1