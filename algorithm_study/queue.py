def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print("Queue is full!!")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("Queue is empty!!")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("Queue is empty!!")
        return None
    return queue[front + 1]

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==> ")

    while select.lower() != 'x':
        if select.lower() == 'i':
            data = input("입력 데이터 ==> ")
            enQueue(data)
            print("큐 상태: ", queue)
        elif select.lower() == 'e':
            data = deQueue()
            print("추출된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        elif select.lower() == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("큐 상태 : ", queue)
        else:
            print("입력이 잘못됨")
        
        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==> ")
    
    print("프로그램 종료!!")    

# 꽉 찬 queue에서 전부 추출되었을경우 초기화하는 내용 추가 필요    