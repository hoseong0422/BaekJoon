def solution(my_string):
    answer = []
    num = ''
    for i in range(len(my_string)):
        if my_string[i].isalpha() == False:
            num += my_string[i]
            print(num)
            if i != len(my_string)-1 and my_string[i+1].isalpha() == True:
                answer.append(int(num))
                num = ''
            elif i == len(my_string)-1:
                answer.append(int(num))
    print(answer)
    return sum(answer)