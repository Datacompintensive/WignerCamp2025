import torch

def find_smallest_abs_eigenvector(matrix: torch.Tensor) -> torch.Tensor:
    """
    Given a real symmetric matrix, return the eigenvector corresponding to the eigenvalue
    with the smallest absolute value.

    Parameters:
        matrix (torch.Tensor): A real symmetric matrix of shape (n, n).

    Returns:
        torch.Tensor: A normalized eigenvector as a 1D tensor.
    """
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.linalg.eigh(matrix)

    # Find the index of the smallest absolute eigenvalue
    min_idx = torch.argmin(eigenvalues.abs())

    # Extract and normalize the corresponding eigenvector
    eigenvector = eigenvectors[:, min_idx]
    eigenvector = eigenvector / torch.norm(eigenvector)

    return eigenvector