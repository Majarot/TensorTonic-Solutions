import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    m = np.asarray(matrix)
    l = 0.000000001
    norm_map = {"l1": lambda x: np.sum(np.abs(x), axis=axis, keepdims=True), "l2":lambda x: np.sum(x**2, axis=axis, keepdims=True)**0.5, "max": lambda x: np.max(x, axis=axis, keepdims=True)}
    return m / (norm_map[norm_type](m) + l)