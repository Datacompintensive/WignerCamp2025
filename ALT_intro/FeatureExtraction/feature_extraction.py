import torch

def mean_all(x: torch.Tensor) -> float:
    """
    Compute the mean of all elements in a 2D tensor.

    Args:
        x (torch.Tensor): A 2D tensor.

    Returns:
        float: The mean of all elements.
    """
    # TODO: Implement this function
    pass

def mean_percentile(x: torch.Tensor, q: float) -> float:
    """
    For each row of x, compute the q-th percentile, then return the mean of these percentiles.

    Args:
        x (torch.Tensor): A 2D tensor.
        q (float): The quantile to compute (between 0 and 1).

    Returns:
        float: Mean of row-wise q-th percentiles.
    """
    # TODO: Implement this function
    pass
