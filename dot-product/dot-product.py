import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    # we will first convert the list into numpy array in float
    x_array = np.asarray(x , dtype = float)
    y_array = np.asarray(y , dtype = float)

    # make dot product
    result = np.dot(x_array, y_array)
    return float(result)