def times_seven(int):
    return int * 7

def squared(int):
    return int * int

def cubed(int):
    return int ** 3

def plus_two(int):
    return int + 2

def times_two(int):
    return int + int

def calculate(int, f):
    return f(int)

print(calculate(2, times_seven))
print(calculate(4, cubed))
print(calculate(5, plus_two))
print(calculate(175, times_two))
print(calculate(12, squared))