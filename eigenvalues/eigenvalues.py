import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    m = np.asarray(matrix)
    eigen = np.linalg.eigvals(m).real
    return np.sort(eigen)