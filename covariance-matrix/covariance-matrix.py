import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x = np.asarray(X)
    x_norm = x - x.mean(axis=0, keepdims=True)
    cov = x_norm.T.dot(x_norm) / (x.shape[0] - 1)
    return cov