# Eigenvector Finder for Symmetric Matrices

This exercise is designed to help students practice working with symmetric matrices and eigenvalue decomposition using PyTorch.

## Task

Write a function that takes a real symmetric matrix as a `torch.Tensor` and returns the eigenvector corresponding to the eigenvalue with the smallest absolute value.

### Requirements

- Use only PyTorch for linear algebra.
- The matrix is guaranteed to be real and symmetric.
- Return a unit-norm eigenvector.

### Files

- `eigenvector_finder.py`: Script to implement your function.
- `test_eigenvector_finder.py`: Pytest-based test suite.
- `solution.py`: Contains a correct solution for reference.

## How to Run

Test the solution with:

```bash
pytest test_eigenvector_finder.py
