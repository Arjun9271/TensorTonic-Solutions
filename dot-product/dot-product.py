import numpy as np

def dot_product(x: list, y: list) -> float:
    a = np.array(x)
    b = np.array(y)
  

    return float(np.dot(a,b))