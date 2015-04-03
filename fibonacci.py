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

    def fast_fib(self, n):
        """ Solves the problem on O(log n) """
        if n == 0:
            return (0, 1)

        a, b = self.fast_fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)

        return (d, c + d)

fib = Fibonacci()
print fib.fib(6)
print fib.fast_fib(6)[0]
