import numpy as np
import torch

def generate_symmetric_matrix_with_eigenvalues(lambda1, lambda2):
    """
    Generates a 2x2 matrix with given eigenvalues lambda1 and lambda2.
    
    Note: as written, this does NOT guarantee the matrix is symmetric
    because Q is not necessarily orthogonal (the fixed Q below is not).
    """
    # Random angle theta in [0, 2π)
    theta = np.random.uniform(0, 2*np.pi)
    
    # Orthogonal rotation matrix Q (should be used to keep symmetry)
    Q = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    # Overwriting Q with a fixed matrix (which is NOT orthogonal)
    Q = np.array([[2, -0.5],
                  [1, 1]])
    
    # Diagonal matrix with the desired eigenvalues
    D = np.diag([lambda1, lambda2])
    
    # Compute the matrix: A = Q D Q^{-1}
    # This ensures A has the specified eigenvalues, but A may not be symmetric
    A = Q @ D @ np.linalg.inv(Q)
    return A

# Example eigenvalues to generate the matrix
eigenvalue1 = 1
eigenvalue2 = 2

# Generate the matrix
A = generate_symmetric_matrix_with_eigenvalues(eigenvalue1, eigenvalue2)

# Convert to PyTorch tensor
A = torch.tensor(A, dtype=float)

# Compute and print eigenvalues and eigenvectors of the generated matrix
eigvals, eigvecs = torch.linalg.eig(A)
print("Eigenvalues and eigenvectors:")
print(eigvals)
print(eigvecs)

# Print the generated matrix
print("Generated matrix:")
print(A)