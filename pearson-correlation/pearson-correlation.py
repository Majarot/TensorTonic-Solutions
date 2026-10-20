import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    x = np.asarray(X)
    
    x_scaled = x - x.mean(axis=0, keepdims=True)
    c = x_scaled.T.dot(x_scaled) / (x_scaled.shape[0])
    
    stds = np.std(x, axis=0, keepdims=True)
    return c / (stds.T.dot(stds))