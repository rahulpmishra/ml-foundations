import numpy as np

# code here
arr1 = np.arange(3*2*2).reshape(3,2,2)
arr2 = np.arange(2*2).reshape(2,2)

def check_broadcast(a,b):
  a = a.copy()
  b = b.copy()
  if len(a)>len(b):
    for _ in range(len(a)-len(b)):
      b.insert(0,1)
  else:
    for _ in range(len(b)-len(a)):
      a.insert(0,1)
    

  for i,v in enumerate(b):
      if v==1:
        b[i] = a[i]
  
  for i,v in enumerate(a):
      if v==1:
        a[i] = b[i]
  
  return a==b 

print(check_broadcast(list(arr1.shape),list(arr2.shape)))
print(arr1)
print(arr2)
print(arr1+arr2)