import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return value
    return wrapper

@timer
def rand_func(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(rand_func(125000000))