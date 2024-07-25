class CustomQueue:
    def __init__(self, SIZE):
        self.queue = [None for _ in range(SIZE)]
        self.SIZE = SIZE
        self.front = -1
        self.rear = -1
    
    def isQueueFull(self):
        if self.rear == self.SIZE - 1:
            if self.front == self.rear:
                if self.queue[self.rear] == None:
                    self.queue = [None for _ in range(self.SIZE)]
                    self.rear = self.front = -1
                    return False
            else:
                if self.front != -1:
                    self.queue = self.queue[self.front + 1:] + [None for _ in range(self.fornt + 1)]
                    self.rear -= self.front + 1
                    self.front = -1
                    return False
                else:
                    return True
        else:
            return False

    def isQueueEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def eneQueue(self, input_data):
        # queue full check
        if self.isQueueFull():
            print("Queue is Full!!")
            return
        self.rear += 1
        self.queue[self.rear] = input_data
    
    def deQueue(self):
        if self.isQueueEmpty():
            print("Queue is Empty!!")
            return
        self.front += 1
        output_data = self.queue[self.front]
        self.queue[self.front] = None
        return output_data
       

# 클래스 큐 작성중 
