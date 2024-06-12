def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        if front == rear:
            if queue[rear] == None:
                queue = [None for _ in range(SIZE)]
                rear = front = -1
                return False
        # 실제 full이 아닌경우 queue를 제일 앞쪽으로 앞당겨서 뒤쪽에 자리 마련 (크기가 컨졌을떄는 안될거같음)
        else:
            if front != -1:
                queue = queue[front+1:] + [None for _ in range(front + 1)]
                rear -= front + 1
                front = -1
                return False
            else:
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
