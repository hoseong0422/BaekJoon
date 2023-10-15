for _ in range(int(input())):
    data=input()
    answer=0
    for i in range(len(data)):
        if i%2==0 :
            temp=2 * int(data[i])
            if temp >= 10: 
                temp= temp % 10 + temp // 10
            answer+=int(temp)
        else: answer += int(data[i])
    if answer % 10==0:
        print("T")
    else: 
        print("F")