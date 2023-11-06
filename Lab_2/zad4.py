
class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step >= self.steps:
            raise StopIteration
        else:
            self.current_step += 1
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result


# Przykład użycia:
fib = Fibonacci(steps=10)

for num in fib:
    print(num)

for i in Fibonacci(steps=7):
    print("\ti=", i)
