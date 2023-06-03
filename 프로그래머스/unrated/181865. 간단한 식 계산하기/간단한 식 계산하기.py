def solution(binomial):
    answer = 0
    if ' + ' in binomial:
        data = binomial.split(' + ')
        a = int(data[0])
        b = int(data[-1])
        return a + b
    elif ' - ' in binomial:
        data = binomial.split(' - ')
        a = int(data[0])
        b = int(data[-1])
        return a - b
    elif ' * ' in binomial:
        data = binomial.split(' * ')
        a = int(data[0])
        b = int(data[-1])
        return a * b
        
    return answer