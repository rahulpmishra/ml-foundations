import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 0, 2  , 0, 2])

# Predict each BEFORE running — write your answer in comments
print(a + b)              # ?
print(a * b)              # ?
print(a / b)              # what happens when dividing by 0?
print(a ** 2)             # ?
print(a > 3)              # ?
print(a[a > 3])           # ?
print(np.where(a > 3, a, 0))   # ?
print(a.cumsum())         # ?
print(a[::-1])            # ?

m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.T)                # ?
print(m.T.shape)          # ?
print(m.sum())            # ?
print(m.sum(axis=0))      # ?
print(m.sum(axis=1))      # ?
print(m.reshape(-1))      # ?
print(m.flatten())        # ?

x = np.ones((3, 1))
y = np.ones((1, 4))
print((x + y).shape)      # ?
print(x + y)              # ?

arr = np.array([5, 3, 8, 1, 9, 2])
print(arr)
print(np.sort(arr))       # ?
print(np.argsort(arr))    # ?  ← very important for ML ranking
print(arr[np.argsort(arr)])  # ?  same as np.sort but via indices