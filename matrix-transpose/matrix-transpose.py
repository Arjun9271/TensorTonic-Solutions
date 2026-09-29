import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    a = np.array(A)
    res = a.T

    return res