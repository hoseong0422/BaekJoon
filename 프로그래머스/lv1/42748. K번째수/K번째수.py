def solution(array, commands):
    answer = []
    for t in range(len(commands)):
        arr = commands[t]
        i = arr[0]
        j = arr[1]
        k = arr[2]
        
        target_array = array[i-1:j]
        target_array.sort()
        answer.append(target_array[k-1])
        
    return answer