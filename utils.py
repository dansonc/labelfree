import numpy as np

def find_alpha_beta(array1, array2):
    A = np.ones((5, 2))
    A[:, 0] = array1
    x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(array2)
    return x[0], x[1]
