import time
import sys
import tracemalloc

# List - compute everything → store everything → then use

# Generator - compute one → use → compute next → use → ...

# ----------------------------- part 1 --------------------------------


# ----------------------------- functions -----------------------------

def square_list(n):
    return [i * i for i in range(n)]

def square_gen(n):
    for i in range(n):
        yield i * i

# ----------------------------- settings -----------------------------

N = 10_000_00   # adjust if system is slow

# ============================= LIST =================================

tracemalloc.start()

start = time.perf_counter()
lst = square_list(N)
end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("LIST VERSION")
print(f"Time taken           : {end - start:.4f} sec")
print(f"Current memory usage : {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage    : {peak / 1024 / 1024:.2f} MB")
print(f"First 10 values       : {lst[:10]}")

print("-" * 70)

# =========================== GENERATOR ===============================

tracemalloc.start()

start = time.perf_counter()
gen = square_gen(N)

first_10 = []
for i in range(5):
    first_10.append(next(gen))
for i, val in enumerate(gen):
    if i < 5:
        first_10.append(val)
end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("GENERATOR VERSION")
print(f"Time taken           : {end - start:.4f} sec")
print(f"Current memory usage : {current / 1024 / 1024:.6f} MB")
print(f"Peak memory usage    : {peak / 1024 / 1024:.6f} MB")
print(f"First 10 values       : {first_10}")

# Lists compute and store all values upfront, while generators produce values lazily.
# When all values are processed, lists are usually faster, but generators save memory.

print("-" * 70)

# ----------------------------- part 2 --------------------------------

# List comprehension - same as above
# Tuple comprehension - shorthand for generator

# List comprehension — loads everything into memory
all_at_once = [x ** 2 for x in range(N)] 
print(f"List size in memory: {sys.getsizeof(all_at_once)/ 1024 / 1024:.6f} MB")

# Generator — processes one item at a time
lazy  = (x ** 2 for x in range(N)) 
print(f"Generator size in memory: {sys.getsizeof(lazy)/ 1024 / 1024:.6f} MB")

print("-" * 70)

final_mess = '''Final takeaway:
   LIST COMPREHENSION → faster but memory-heavy
   GENERATOR          → memory-efficient but slightly slower'''
print(final_mess)