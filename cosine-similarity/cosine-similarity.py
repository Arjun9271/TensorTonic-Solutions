import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.array(a)
    b = np.array(b)

    dot_pro = np.dot(a,b)
    
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return float(dot_pro/(mag_a*mag_b))
    