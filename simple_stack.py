class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def __str__(self):
        return self.data.__str__()
