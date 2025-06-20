# 🧠 ALT_intro

This directory contains two introductory programming assignments designed to help students develop the essential skills used in the **ALT (Adaptive Law-based Transformation)** method for time series classification. Each task includes:

- 📄 A problem description in a `README.md` file
- ✍️ A Python script with missing functions to be implemented
- ✅ A reference solution
- 🧪 A test script compatible with `pytest` to validate correctness

These exercises provide hands-on experience with core mathematical and computational techniques used in the ALT feature extraction pipeline.

---

## 📂 Assignments

### 🔹 [Eigenvector](Eigenvector)

**Goal**: Compute the eigenvector corresponding to the smallest (absolute value) eigenvalue of a real symmetric matrix using PyTorch.
- `find_smallest_abs_eigenvector`: Returns the correct law.

| File | Purpose |
|------|---------|
| [Eigenvector/README.md](Eigenvector/README.md) | Task description and example |
| [eigenvector_finder.py](Eigenvector/eigenvector_finder.py) | File to implement the solution |
| [eigenvector_finder_solution.py](Eigenvector/eigenvector_finder_solution.py) | Correct reference solution |
| [test_eigenvector_finder.py](Eigenvector/test_eigenvector_finder.py) | Unit tests with `pytest` |

---

### 🔹 [FeatureExtraction](FeatureExtraction)

**Goal**: Implement two feature extraction methods for 2D `torch.Tensor` inputs:
- `mean_all`: Compute the mean of all elements.
- `mean_percentile`: Compute the q-th percentile of each row, then return the mean of these percentiles.

| File | Purpose |
|------|---------|
| [FeatureExtraction/README.md](FeatureExtraction/README.md) | Task description and examples |
| [feature_extraction.py](FeatureExtraction/feature_extraction.py) | File to implement the solution |
| [feature_extraction_solution.py](FeatureExtraction/feature_extraction_solution.py) | Correct reference solution |
| [test_feature_extraction.py](FeatureExtraction/test_feature_extraction.py) | Unit tests with `pytest` |

---

## 🧪 Running the Tests

Make sure you have `pytest` installed. Then run the tests with:

```bash
pytest test_[FILE].py
