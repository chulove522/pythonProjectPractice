class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def Push(self, data):
        self.stack.append(data)
        self.size += 1

    def Pop(self):
        if self.size == 0:
            print('stack is empty')
        else:
            self.stack.pop()
            self.size -= 1

    def Top(self):
        if self.size == 0:
            print('stack is empty')
            return 0
        else:
            return self.stack[self.size - 1]

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size


class Solution:
    def isValid(self, s: str) -> bool:
        #x = ('(',')','[',']','{','}')
        stack = Stack()
        for st in s:
            print("st是",st)
            if st == '(':
                stack.Push(st)
            elif st == '[':
                stack.Push(st)
            elif st == '{':
                stack.Push(st)
            elif st == ')' and stack.Top()== '(':
                stack.Pop()
            elif st == ']' and stack.Top()== '[':
                stack.Pop()
            elif st == '}' and stack.Top() == '{':
                stack.Pop()
            else:
                return False

        if stack.getSize() != 0:
            return False
        else:
            return True

s = Solution()
print("1: " , s.isValid("{()[]{}}"))
print("2: " , s.isValid("{()]]"))