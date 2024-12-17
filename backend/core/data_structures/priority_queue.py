import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, data):
        heapq.heappush(self.queue, (priority, data))

    def pop(self):
        return heapq.heappop(self.queue) if self.queue else None

    def peek(self):
        return self.queue[0] if self.queue else None
