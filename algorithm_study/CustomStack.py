# 클래스로 스택 만들기!!

class CustomStack:
    def __init__(self, SIZE):
        self.stack = [None for _ in range(SIZE)]
        self.top = -1
        self.SIZE = SIZE

    def isStackFull(self):
        if self.top >= self.SIZE - 1:
            return True
        else:
            return False
        
    def isStackEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self, data):
        if self.isStackFull():
            print("Stack is full!!")
            return self.stack
        else:
            self.top += 1
            self.stack[self.top] = data
            return self.stack
    
    def pop(self):
        if self.isStackEmpty():
            print("Stack is empty!!")
            return None, self.stack
        else:
            pop_data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return pop_data, self.stack
    
    def peek(self):
        if self.isStackEmpty():
            print("Stack is empty!!")
            return None, self.stack
        else:
            return self.stack[self.top], self.stack
        
if __name__ == "__main__":
    stack_size = int(input())
    stack = CustomStack(stack_size)
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==>")

    while select.lower() != 'x':
        # 삽입
        if select.lower() == 'i':
            data = input("입력할 데이터 ==>")
            print("스택 상태 :", stack.push(data))
        # 제거
        elif select.lower() == 'e':
            pop_data, stack_state = stack.pop()
            print("제거된 데이터 :", pop_data)
            print("스택 상태 :", stack_state)
        # 확인
        elif select.lower() == 'v':
            data, stack_state = stack.peek()
            print("확인된 데이터 ==>", data)
            print("스택 상태 :", stack_state)

        else:
            print("잘못된 입력")
        
        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나를 선택 ==>")

    print("종료")