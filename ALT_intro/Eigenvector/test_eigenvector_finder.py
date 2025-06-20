import torch
import pytest
from eigenvector_finder import find_smallest_abs_eigenvector

def test_identity_matrix():
    A = torch.eye(3)
    v = find_smallest_abs_eigenvector(A)
    assert torch.allclose(torch.norm(v), torch.tensor(1.0), atol=1e-6)
    assert torch.allclose(A @ v, v, atol=1e-6)

def test_known_eigenvector():
    A = torch.tensor([[2.0, 0.0], [0.0, -0.1]])
    v = find_smallest_abs_eigenvector(A)
    # Smallest abs eigenvalue is -0.1, eigenvector is [0, 1] or [0, -1]
    expected = torch.tensor([0.0, 1.0])
    assert torch.allclose(v.abs(), expected, atol=1e-5)

def test_symmetric_random():
    torch.manual_seed(0)
    M = torch.randn(5, 5)
    A = (M + M.T) / 2  # Symmetrize
    v = find_smallest_abs_eigenvector(A)
    assert v.shape == (5,)
    assert torch.allclose(torch.norm(v), torch.tensor(1.0), atol=1e-6)
    # Check v is an eigenvector
    Av = A @ v
    lambda_v = torch.dot(v, Av)
    assert torch.allclose(Av, lambda_v * v, atol=1e-5)
