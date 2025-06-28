# WignerCamp2025

This repository contains the educational materials for the **2025 Wigner Summer Camp** organized by the **Data and Compute Intensive Sciences Research Group** at the Wigner Research Centre for Physics.

The camp is designed for high school students and introduces the mathematical and computational foundations of **time series classification**, culminating in practical sessions using the **ALT method**.

---

## 🔍 About the Method

The core method of the camp is the **Adaptive Law-based Transformation (ALT)** — a lightweight, interpretable, and efficient feature representation technique for time series classification. ALT builds on the earlier LLT method and provides state-of-the-art performance with minimal tuning.

- 📄 ALT preprint: [arXiv:2501.09217](https://arxiv.org/abs/2501.09217)
- 📄 ALT software description: [arXiv:2504.12841](https://arxiv.org/abs/2504.12841)
- 🧠 Official Python package: [github.com/Datacompintensive/ALT](https://github.com/Datacompintensive/ALT)

---

## 📦 Repository Structure

You can clone this repository using:

```bash
git clone https://github.com/Datacompintensive/WignerCamp2025.git
cd WignerCamp2025
```

### Contents

You should get familiar with the folders in this repository in the following order:

| Folder | Description |
|--------|-------------|
| [BasicProgramming](./BasicProgramming) | Exercises and materials on basic Python programming. |
| [Mathematics](./Mathematics) | Linear algebra essentials for data transformations. |
| [Terminal](./Terminal) | Basic linux terminal and `vim` commands. |
| [ALT_intro](./ALT_intro) | Introduction to time series classification and the ALT method. |

---

## 🐍 Creating the Conda Environment

To run the Python scripts, create a new Conda environment named `ALTenv`:

```bash
conda create -n ALTenv python=3.11 -y
conda activate ALTenv
```

Then install the required packages:

```bash
pip install numpy matplotlib pandas scipy
pip install torch torchvision torchaudio
pip install pytest
```

---

## 📄 Building LaTeX Documents

Some folders contain `.tex` slides or documents. To compile all LaTeX files using `CMake`:

```bash
mkdir build
cd build
cmake ..
cmake --build . -j4
cd -
```

This will:

- Compile all `.tex` files found in the subdirectories,
- Automatically handle references (BibTeX if needed),
- Clean up all temporary files including: `.aux`, `.log`, `.toc`, `.out`, `.bbl`, `.blg`, `.lof`, `.lot`, `.snm`, `.nav`, `.vrb`.

---

## 👥 Authors

Developed by members of the **Wigner Data and Compute Intensive Sciences Group**.

---

## 📜 License

Materials in this repository are provided for **educational purposes**. For usage beyond the camp, please contact the authors.