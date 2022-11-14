def solution(my_string):
    data = my_string.split()
    answer = int(data[0]) 

    for i in range(1, len(data), 2):
        if data[i] == "+":
            answer += int(data[i+1]) 
        else:
            answer -= int(data[i+1])

    return answer
