import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x)
    return float((x.mean() - mu0) / (x.std(ddof=1) / len(x)**0.5))