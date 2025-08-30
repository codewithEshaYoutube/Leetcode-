from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate so new element comes to front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  # now top is always at front

    def top(self) -> int:
        return self.q[0]  # since we rotated, top is at front

    def empty(self) -> bool:
        return len(self.q) == 0
