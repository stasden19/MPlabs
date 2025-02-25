class PriorityQueue:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = PriorityQueue(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = PriorityQueue(value)
            else:
                self.right.insert(value)

    def _find_max(self):
        if self.right:
            return self.right._find_max()
        return self

    def _remove_max(self, parent):
        if self.right:
            return self.right._remove_max(self)
        if parent:
            parent.right = self.left
        return self.value

    def output(self):
        if self.right:
            return self._remove_max(None)
        else:
            value = self.value
            if self.left:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            else:
                raise ValueError("Очередь пуста!")
            return value


# Пример использования
pq = PriorityQueue(123)
pq.insert(456)
pq.insert(12)
pq.insert(23)

print(pq.output())
print(pq.output())
