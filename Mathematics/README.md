# 📐 Mathematics

This folder contains two educational LaTeX-based presentations designed for the Wigner Summer Camp. These presentations cover essential mathematical foundations and evaluation techniques for time series classification. All documents can be built using the provided `CMakeLists.txt`, which automatically compiles the `.tex` files to `.pdf`, handling references and cleanup.

## 📊 Presentations and Notebooks

| PDF File | Description | Source File |
|----------|-------------|-------------|
| [linear_algebra.pdf](linear_algebra.pdf) | Covers basic concepts in linear algebra, including vectors, matrices, dot products, matrix multiplication, geometric interpretation, and eigendecomposition. | [linear_algebra.tex](linear_algebra.tex) |
| [TSC.pdf](TSC.pdf) | Introduces the time series classification (TSC) problem. Discusses evaluation metrics such as accuracy, precision, recall, and F1 score, with illustrative confusion matrix examples. | [TSC.tex](TSC.tex) |
| | Provides hands on exercises for the important scientific computing concepts: dot product, vector-matrix and matrix-matrix multiplication, and precentiles. | [ComputingExercises.ipynb](ComputingExercises.ipynb) |
| | Gives the solutions for the exercies in [ComputingExercises.ipynb](ComputingExercises.ipynb). | [ComputingExercises_solution.ipynb](ComputingExercises_solution.ipynb) |

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

All citations and bibliography data are stored in the [references.bib](references.bib) file. The `CMake` compiles all the `.tex` files to `.pdf` files bith with and without the need for bibliography.

---

© 2025 Wigner Research Centre for Physics – Data and Compute Intensive Sciences Group