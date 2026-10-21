import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmfs = [math.exp(-lam) * lam**i / math.factorial(i) for i in range(k+1)]
    return  {"pmf": float(pmfs[-1]), "cdf": float(sum(pmfs))}