# Kevin Renaldi Bahari
# 陈凯文
# 202369990129

# pytho code
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


class StackOfMax():
    def __init__(self):
        self.stack = list()

    def Push(self, a):
        if len(self.stack) == 0:
            self.stack.append(a)
        else:
            prev_max = self.stack[-1]
            if a > prev_max:
                self.stack.append(a)
            else:
                self.stack.append(prev_max)

    def Top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return

    def Pop(self):
        assert (len(self.stack))
        self.stack.pop()


if __name__ == '__main__':
    maxStack = StackOfMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            maxStack.Push(int(query[1]))
        elif query[0] == "pop":
            maxStack.Pop()
        elif query[0] == "max":
            print(maxStack.Top())
        else:
            assert (0)