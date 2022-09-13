N = int(input())
init = 666
cnt = 0
while True:    
    if '666' in str(init):  
        cnt += 1    
    if N == cnt:
        print(init)
        break
    init += 1