import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    my_array = np.array(x) * -1
    result_array = 1 / (1+ np.exp(my_array))
    return result_array
    

    
    