import numpy as np

def sample_var_std(x: list) -> dict:
    var = np.var(x,ddof = 1)
    st_dev = np.std(x,ddof = 1)


    return {
        "variance": float(var),
        "standard_deviation": float(st_dev)
    }