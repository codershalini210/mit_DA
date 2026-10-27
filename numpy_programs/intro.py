import numpy as np 
numbers = np.array([12,52,65,75])
numbers2D = np.array([
    
        [[12,32,58],[44,32,77]],
      [[32,44,77],[54,23,45]],
    [[1,5,5],[2,5,1]]   
])

print(numbers2D.dtype)
print(np.shape(numbers))
print(np.shape(numbers2D))
print(np.ndim(numbers))
print(np.ndim(numbers2D))
print("size of all element ",(numbers2D.itemsize * np.size(numbers2D)) )
# print("max is ",np.max(numbers))
# print("min is ",np.min(numbers))
# print("length is ",np.size(numbers))
# print("sum is ",np.sum(numbers))
# print("avg is ",np.average(numbers))