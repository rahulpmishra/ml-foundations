### What does pdb.set_trace() do and when would you use it in an ML project?

pdb.set_trace() is used to enter into python debugging mode and debug your program line by line according to execution and is helpful to track down errors in ml pipelines.

Key Points:
- Allows step-by-step execution of code
- Helps inspect variables during runtime
- Useful for understanding program flow

ML Context:
- Debugging shape mismatch errors
- Tracking empty datasets or incorrect values
- Finding NaN/None issues in pipelines

Quick Recall:
Pause → inspect → step → debug


---

### What is the difference between a decorator and a regular function?

A decorator wraps a function modifying its behaviour without changing its original code. With help of a decorator we can add any other functionality on top of a function without changing anything in that original function.

Key Points:
- Wraps another function
- Modifies behavior without editing original code
- Used to add extra functionality (e.g., logging, timing)

ML Context:
- Used in frameworks (e.g., API routes, logging training time)
- Useful for tracking execution or adding monitoring

Quick Recall:
Wrap → modify → no change to original


---

### Why does a generator use less memory than a list?

Generators are memory-efficient because they yield values one at a time instead of storing the entire dataset in memory, unlike lists which allocate all values upfront.
They follow lazy evaluation (compute on demand), whereas lists use eager evaluation.

Generators are usually slower than lists because each value requires:
- resuming the generator state
- executing Python bytecode
- yielding control back to the caller

This repeated pause/resume cycle adds per-iteration overhead.

Lists, on the other hand, use optimized internal loops and contiguous memory allocation, making full computation faster when all elements are needed.

Final takeaway:
- traded speed for memory efficiency  
- LIST → faster but memory-heavy  
- GENERATOR → memory-efficient but slightly slower  

Key Points:
- Lazy evaluation (on-demand)
- No full memory allocation
- Slight iteration overhead

ML Context:
- Used for batch processing large datasets
- Useful when data cannot fit into memory

Quick Recall:
Lazy → memory save → slightly slower


---

### What does __exit__ returning False mean?

A context manager in Python is an object that defines __enter__ and __exit__ methods to manage setup and cleanup of resources automatically using the with statement.

__exit__ returning False means that when any error or exception occurs in code present in with block, then just like a normal program we will be having errors in the terminal and flow of program will break with error or exception whatever occurred.

Key Points:
- __enter__ → setup
- __exit__ → cleanup
- Controls exception behavior

Important:
- return True → suppress exception  
- return False → propagate exception  

ML Context:
- Used in file handling, model loading, resource cleanup
- Ensures proper release of memory/resources

Quick Recall:
False → error shows  
True → error suppressed


---

### What is *args and **kwargs and why does the timer decorator need them?

*args and **kwargs are basically used to receive variable number of arguments into the function. Timer decorator need them to ensure that if any number of arguments either in normal form or key value pair form it gets provided to the function on which we are applying the timer decorator.

Key Points:
- *args → tuple (positional arguments)
- **kwargs → dictionary (keyword arguments)
- Allows flexible function inputs

ML Context:
- Useful in reusable functions and pipelines
- Needed in decorators to support any function signature

Quick Recall:
*args → positional  
**kwargs → keyword