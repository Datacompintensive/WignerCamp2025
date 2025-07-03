# 📐 Mathematics

This folder contains two educational LaTeX-based presentations designed for the Wigner Summer Camp. These presentations cover essential mathematical foundations and evaluation techniques for time series classification. All documents can be built using the provided `CMakeLists.txt`, which automatically compiles the `.tex` files to `.pdf`, handling references and cleanup.

## 📊 Presentations and Notebooks

| PDF File | Description | Source File |
|----------|-------------|-------------|
| [linear_algebra.pdf](linear_algebra.pdf) | Covers basic concepts in linear algebra, including vectors, matrices, dot products, matrix multiplication, geometric interpretation, and eigendecomposition. | [linear_algebra.tex](linear_algebra.tex) |
| [linear_algebra_test.pdf](linear_algebra_test.pdf) | Contains exercises to test the understanding of the most important linear algebra concepts. | [linear_algebra_test.tex](linear_algebra_test.tex) |
| [TSC.pdf](TSC.pdf) | Introduces the time series classification (TSC) problem. Discusses evaluation metrics such as accuracy, precision, recall, and F1 score with illustrative confusion matrix examples. | [TSC.tex](TSC.tex) |
| [miscellaneous_topics.pdf](miscellaneous_topics.pdf) | Details some of the other mathematical concepts which are useful for understanding the method: the precentiles and the linear recursions. | [miscellaneous_topics.tex](miscellaneous_topics.tex) |
| | Provides hands on exercises for the important scientific computing concepts: dot product, vector-matrix and matrix-matrix multiplication, and precentiles. | [ComputingExercises.ipynb](ComputingExercises.ipynb) |
| | Gives the solutions for the exercies in [ComputingExercises.ipynb](ComputingExercises.ipynb). | [ComputingExercises_solution.ipynb](ComputingExercises_solution.ipynb) |

### 📝 Test files

| PDF File | Description | Source File |
|----------|-------------|-------------|
| [linear_algebra_test.pdf](linear_algebra_test.pdf) | Self-check test covering basic linear algebra concepts including vectors, matrix operations, determinants, and eigenproblems. | [linear_algebra_test.tex](linear_algebra_test.tex) |
| [linear_algebra_test_solution.pdf](linear_algebra_test_solution.pdf) | Detailed solutions to the self-check test with step-by-step explanations. | [linear_algebra_test_solution.tex](linear_algebra_test_solution.tex) |
| [linear_algebra_revision_test.pdf](linear_algebra_revision_test.pdf) | More advanced revision test covering extended linear algebra concepts with higher-dimensional problems. | [linear_algebra_revision_test.tex](linear_algebra_revision_test.tex) |
| [linear_algebra_revision_test_solution.pdf](linear_algebra_revision_test_solution.pdf) | Complete solutions to the revision test problems with verifications. | [linear_algebra_revision_test_solution.tex](linear_algebra_revision_test_solution.tex) |

## 🛠 Compilation

To compile the presentations (from this directory):

```bash
mkdir ../build
cd ../build
cmake ..
cmake --build . -j4
cd -
```

This will:

- Compile both LaTeX documents to `.pdf` (even if no bibliography is required),
- Automatically run `bibtex` when needed,
- Clean up all temporary files (`.aux`, `.log`, `.toc`, `.snm`, `.nav`, `.vrb`, etc.).

> **Note**: All figures used in the slides are stored in the [img/](img/) folder.

## 📚 References

All citations and bibliography data are stored in the [references.bib](references.bib) file.

---

© 2025 Wigner Research Centre for Physics – Data and Compute Intensive Sciences Group