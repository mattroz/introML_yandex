import numpy as np

''' generate array with the normal distribution using
    mathematical expectation = loc = 1,
    standard deviation (std_dev) = 10,
    size of matrix = 1000x50
'''
X = np.random.normal(loc=1, scale=10, size=(1000, 50))
print(X)

'''
    matrix normalization: 
    subtract from each column its mean value 
    and divide by column's standard deviation
    (axis = 0 means that the function will do 
    the calculations by columns,
    axis = 1 - by rows)
'''
mean_for_columns = np.mean(X, axis=0)
std_dev_for_columns = np.std(X, axis=0)
X_normalized = ((X - mean_for_columns) / std_dev_for_columns)
print(X_normalized)

'''
    print indices of rows which 
    sum of elements is bigger than 10
'''
Z = np.array([[4, 5, 0],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])
row_sum = np.sum(a=Z, axis=1)
print(np.nonzero(row_sum > 10))


'''
    generate two unit matrices 
    (3x3) and (3x3) and merge them 
    to (6x3) matrix
'''
unit_matrix_1 = np.eye(3, 3)
unit_matrix_2 = np.eye(3, 3)
print(np.vstack((unit_matrix_1, unit_matrix_2)))