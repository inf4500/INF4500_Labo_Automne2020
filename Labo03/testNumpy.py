import numpy as np

# Exemple numpy
#####################################################

matrix = np.zeros((5, 5))
print(matrix); matrix[4][4] = 1; print(matrix)


print('-'*50)
print('-'*50)

# Exemple sans numpy
#####################################################

# OK
lst = [[0 for i in range(5)] for i in range(5) ]
print(lst); lst[4][4] = 1; print(lst)


print('-'*50)

# Pas OK
lst1 = [0, 0, 0, 0, 0]
lst2 = [lst1 for i in range(5) ]
print(lst2); lst2[4][4] = 1; print(lst2)


print('-'*50)

# Pas OK
lst3 = [[0]*5]*5
print(lst3); lst3[4][4] = 1; print(lst3)