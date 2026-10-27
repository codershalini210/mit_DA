import numpy as np
# zeros = np.zeros(5)
# zeros = np.zeros([2,3],int)
# print(zeros)
# ----------------------
# ones = np.ones(3)
# print(ones)
# ones = np.ones([3,2])
# print(ones)
# -------------------
# ary =np.arange(5)
# ary =np.arange(2,6)
# ary =np.arange(2,6,2)
# print(ary)
# --------------------
# random_ary = np.random.random_integers(1,9,5)
# # random_ary = np.random.randint(1,9,4)
# random_ary = np.random.rand()  #single element
# random_ary = np.random.rand(3) # one dimension ary 
# random_ary = np.random.rand(3,2)   # two dimension ary
# print(random_ary)
# ary =np.identity(6)
# ary = np.full([2,2],100)

# ary= np.array([np.random.randint(1,85,5),np.random.randint(1,85,5),np.random.randint(1,85,5)
#                ,np.random.randint(1,85,5),np.random.randint(1,85,5)])

ary = np.random.randint(1, 100, size=(5, 5))
print(ary)
