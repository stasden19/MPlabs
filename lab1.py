class PriorityQueue():


    def __init__(self, value):
        self.all_numbers = [value]
        self.value = value
        self.left = None
        self.right = None

    def __len__(self):
        return len(self.all_numbers)
    def is_empty(self):
        return self.left is None and self.right is None

    def insert(self, value):
        self.all_numbers.append(value)
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


pq = PriorityQueue(123)
pq.insert(456)
pq.insert(12)
pq.insert(23)
print(len(pq))
print(pq.output())
print(pq.output())
print(pq.output())
print(pq.is_empty())
