class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        res = self.stack[len(self.stack)-1]
        _ = self.stack.pop()
        return res

    def check(self):
        try:
            self.stack[-1]
            return self.stack[-1]
        except IndexError:
            return 0

    def check_two_arg(self):
        if (len(self.stack) >= 2):
            return True
        else:
            return False
