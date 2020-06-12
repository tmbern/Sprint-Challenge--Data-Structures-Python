class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None for i in range(self.capacity)]
        self.current = 0

    def append(self, item):
        self.buffer[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0


    def get(self):
        return [i for i in self.buffer if i is not None] 