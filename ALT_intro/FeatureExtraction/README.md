# Feature Extraction with PyTorch

This exercise is designed to help students become familiar with basic tensor operations in PyTorch, focusing on statistical feature extraction.

## Task

You need to implement **two functions** in `feature_extraction.py`:

1. `mean_all(x: torch.Tensor) -> float`:  
   Computes the mean of **all elements** in a 2D tensor.  
   Hint: [torch.mean](https://pytorch.org/docs/stable/generated/torch.mean.html).

2. `mean_percentile(x: torch.Tensor, q: float) -> float`:  
   For each row in the 2D tensor `x`, compute the `q`-th percentile (e.g., 0.05 for 5%) using `torch.quantile`, then return the mean of these percentile values.  
   Hint: [torch.quantile](https://pytorch.org/docs/stable/generated/torch.quantile.html).

### Files

- `feature_extraction.py`: Script to implement your functions.
- `test_feature_extraction.py`: Pytest-based test suite.
- `solution.py`: Contains a correct solution for reference.

## How to Run

Test your solution with:

```bash
cd ALT_intro/FeatureExtraction
pytest test_feature_extraction.py
