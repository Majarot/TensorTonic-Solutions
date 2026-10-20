import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    l = 0.000000001
    res = a.dot(b) / (np.linalg.norm(a)* np.linalg.norm(b) + l)
    return float(res)