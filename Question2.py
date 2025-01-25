'''Write a Python script that generate matrix of (10000, 10000) and transpose it. '''

import numpy as np

def generate_matrix():
    """_summary_

    Returns:
        ndarray: ndarray of size(10000,10000)
    """
    x=np.random.randint(200 ,size=(10000,10000))
    return x

def main_function():
    # generating the matrix of size (10000,10000)
    mat=generate_matrix()
    print(mat)
    
    print("Transpose of the given matrix")
    # transpose of the matrix
    mat2=mat.T
    print(mat2)
    
    
if __name__=='__main__':
    main_function() 