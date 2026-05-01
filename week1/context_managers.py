class Demo:
    def __enter__(self):
        print('1. __enter__ runs')
        return "hello from enter"
    
    def __exit__(self, exc_type, exc, tb):
        print('3. __exit__ runs')
        print('exc_type: ',exc_type)
        return False
    
with Demo() as val:
    print('2. Inside block, val = ',val)

print('---------------------------------------------------------------')

class ErrorDemo1:
    def __enter__(self):
        print('enter runs')
    
    def __exit__(self,exc_type,exc, tb):
        print('exit runs')
        print('exc_type: ',exc_type)
        print('exc: ',exc)
        print('tb: ',tb)
        return True

with ErrorDemo1():
    print('with block statements run')
    print(1/0)

print('---------------------------------------------------------------')

class ErrorDemo2:
    def __enter__(self):
        print('enter runs')
    
    def __exit__(self,exc_type,exc, tb):
        print('exit runs')
        print('exc_type: ',exc_type)
        print('exc: ',exc)
        print('tb: ',tb)
        return False

with ErrorDemo2():
    print('with block statements run')
    print(1/0)


# after class Demo creation, when `with Demo() as val` runs:

# 1. First, a Demo object is created.
# 2. Then `__enter__()` is automatically called.
# 3. Whatever `__enter__()` returns is stored in `val`.
#    → here: val = "hello from enter"

# 4. Next, the code inside the `with` block executes:
#    → print('2. Inside block, val = ', val)

# 5. After the block finishes (whether normally or due to an error),
#    `__exit__(exc_type, exc, tb)` is automatically called.

# 6. The parameters of `__exit__`:
#    - exc_type → type of exception (e.g., ZeroDivisionError)
#    - exc      → actual exception object(i.e. exception message that we see)
#    - tb       → traceback object

#    If no exception occurs:
#    → exc_type = None, exc = None, tb = None

# 7. The return value of `__exit__` controls exception handling:
#    - return False → do NOT suppress the exception (normal behavior)
#    - return True  → suppress the exception (program continues without crash)
#    - when error occured and return = True is present then program will not break and finish as normal without errors
#    - when error occured and return = False is present then program will break and show error in terminal like normal 

# So overall flow:
#     create object → __enter__ → assign to val → run block → __exit__


