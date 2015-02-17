fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)

print fib(6)

class Fibonacci(object):
    def __init__(self):
        self.__cache = [1, 1]

    def fib(self, pos):
        pos -= 1
        if pos >= len(self.__cache):
            last_pos = len(self.__cache) - 1
            while last_pos != pos:
                last_pos += 1
                self.__cache.append(self.__cache[last_pos-1] + self.__cache[last_pos-2])

        return self.__cache[pos]

fib = Fibonacci()
print fib.fib(6)
