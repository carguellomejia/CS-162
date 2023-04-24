import numpy as np
array1 = np.random.randint(1, 50, size=(5, 5), dtype=int)
print(array1)
print(array1.shape)

for row in array1:
    for item in row:
        print(item)
print(array1[1][2])
q = np.mean(array1, axis = 1)
print(q)
q_add = np.sum(array1, axis = 0)
print(q_add[0], q_add[1], q_add[2], q_add[3], q_add[4])