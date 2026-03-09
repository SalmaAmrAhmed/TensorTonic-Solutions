import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    
    rows = len(A)
    cols = len(A[0])
    
    A_T = np.ones((cols, rows))


    i = 0
    while i < rows:
        j = 0
        while j < cols:
            A_T[j][i] = A[i][j]
            j+=1
        i+=1

    return A_T

     
        
