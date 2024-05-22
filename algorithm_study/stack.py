def isStackFull():
    global SIZE, stack, top

    if top >= SIZE - 1:
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top

    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top

    if isStackFull():
        print("Stack is full!!")
        return
    top += 1
    stack[top] = data

def pop(data):
    global SIZE, stack, top

    if isStackEmpty():
        print("Stack is empty!!")
        return None
    data =  stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top

    if isStackEmpty():
        print("Stack is empty!!")
        return None
    return stack[top]

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==>")

    while select.lower() != 'x':
        
        # 삽입
        if select.lower() == 'i':
            data = input("입력할 데이터 ==>")
            push(data)
            print("스택 상태 :", stack)
        
        elif select.lower() == 'e':
            data = pop(data)
            print("제거된 데이터 :", data)
            print("스택 상태 :", stack)

        elif select.lower() == 'v':
            data = peek()
            print("확인된 데이터 ==>", data)
            print("스택 상태 :", stack)

        else:
            print("잘못된 입력")
        
        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==>")

    print("종료")
