class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        flag = False
        if len(self.stack) != 0:
            flag = True
        return flag

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        elem = None
        if len(self.stack) != 0:
            elem = self.stack.pop()
        return elem

    def peek(self):
        elem = None
        if len(self.stack) != 0:
            elem = self.stack[-1]
        return elem

    def size(self):
        return len(self.stack)

open_brackets = ['(', '{', '[']
close_brackets = [')', '}', ']']

check = Stack()

def check_brackets(item):
    for i in item:
        if i in open_brackets:
            check.push(i)
        elif i in close_brackets:
            ind = close_brackets.index(i)
            if check.size() > 0 and open_brackets[ind] == check.peek():
                check.pop()
            else:
                return 'Несбалансированно'
    if not check.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

print(check_brackets(input()))