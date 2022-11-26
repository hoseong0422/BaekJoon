def solution(price, money, count):
    total = [price * i for i in range(1, count+1)]
    
    if sum(total) > money:
        return sum(total) - money
    else:
        return 0