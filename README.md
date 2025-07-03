# WignerCamp2025

This repository contains the educational materials for the **2025 Wigner Summer Camp** organized by the **Data and Compute Intensive Sciences Research Group** at the Wigner Research Centre for Physics.

The camp is designed for high school students and introduces the mathematical and computational foundations of **time series classification**, culminating in practical sessions using the **ALT method**.

---

## ⏰ Recommended timeline

<body>
    <table>
        <tr>
            <th>Time</th>
            <th>Day 1</th>
            <th>Day 2</th>
            <th>Day 3</th>
            <th>Day 4</th>
            <th>Day 5</th>
        </tr>
        <tr>
            <td class="time-column">9:00-9:30</td>
            <td>Opening Ceremony</td>
            <td>Revision Exercises</td>
            <td>Introduction to the choosen topic</td>
            <td rowspan="7">Working on the choosen topic <i>(anomaly detection or fewer laws)</i></td>
            <td rowspan="4">Creating Presentation</td>
        </tr>
        <tr>
            <td class="time-column">9:30-10:00</td>
            <td>Introduction</td>
            <td><a href="./Terminal/Vim.md">Introduction to VIM</a></td>
            <td rowspan="6">Working on the choosen topic <i>(anomaly detection or fewer laws)</i></td>
        </tr>
        <tr>
            <td class="time-column">10:00-10:30</td>
            <td rowspan="5"><a href="./BasicProgramming/">Basic Programming</a> + <a href="./Terminal/Git.md">Short introduction to Git & GitHub</a></td>
            <td rowspan="2"><a href="./ALT_intro/Eigenvector/">ALT introduction - Find the smallest eigenvector</a></td>
        </tr>
        <tr>
            <td class="time-column">10:30-11:00</td>
        </tr>
        <tr>
            <td class="time-column">11:00-11:30</td>
            <td><a href="./ALT_intro/FeatureExtraction/">ALT introduction - Feature Extraction</a></td>
            <td rowspan="2">Finalizing Presentation</td>
        </tr>
        <tr>
            <td class="time-column">11:30-12:00</td>
            <td rowspan="2"><a href="./ALT/">The Method - ALT</a></td>
        </tr>
        <tr>
            <td class="time-column">12:00-12:30</td>
            <td>Practice Presentation</td>
        </tr>
        <tr>
            <td class="time-column">12:30-13:00</td>
            <td rowspan="2">Lunch</td>
            <td rowspan="2">Lunch</td>
            <td rowspan="2">Lunch</td>
            <td rowspan="2">Lunch</td>
            <td rowspan="2">Lunch</td>
        </tr>
        <tr>
            <td class="time-column">13:00-13:30</td>
        </tr>
        <tr>
            <td class="time-column">13:30-14:00</td>
            <td rowspan="3"><a href="./Mathematics/linear_algebra.pdf">Introduction to Linear Algebra</a></td>
            <td rowspan="3">Running ALT on TSC <i>(& choosing r, l, k values)</i></td>
            <td rowspan="3">Non project related activity (visiting nuclear reactor)</td>
            <td rowspan="6">Working on the choosen topic <i>(anomaly detection or fewer laws)</i></td>
            <td  rowspan="10">Closing & presentation</td>
        </tr>
        <tr>
            <td class="time-column">14:00-14:30</td>
        </tr>
        <tr>
            <td class="time-column">14:30-15:00</td>
        </tr>
        <tr>
            <td class="time-column">15:00-15:30</td>
            <td rowspan="2"><a href="./Mathematics/miscellaneous_topics.pdf">Introduction to Percentiles and Linear Recursion</a> <br><a href="./Mathematics/TSC.pdf">Introduction to TSC</a></td>
            <td rowspan="3"><a href="./TestsAndDocumentation/">Writing tests for ALT<a></td>
            <td rowspan="2">Working on the choosen topic <i>(anomaly detection or fewer laws)</i></td>
        </tr>
        <tr>
            <td class="time-column">15:30-16:00</td>
        </tr>
    </table>
</body>
</html>

## 🔍 About the Method

The core method of the camp is the **Adaptive Law-based Transformation (ALT)** — a lightweight, interpretable, and efficient feature representation technique for time series classification. ALT builds on the earlier LLT method and provides state-of-the-art performance with minimal tuning.

- **ALT Preprint**  
  *Marcell T. Kurbucz, Balázs Hajós, Balázs P. Halmos, Vince Á. Molnár, Antal Jakovác*.  
  *Adaptive Law-Based Transformation (ALT): A Lightweight Feature Representation for Time Series Classification.*  
  arXiv preprint: [arXiv:2501.09217](https://arxiv.org/abs/2501.09217) (2025).

- **ALT Software Package**  
  *Balázs P. Halmos, Balázs Hajós, Vince Á. Molnár, Marcell T. Kurbucz, Antal Jakovác*.  
  *ALT: A Python Package for Lightweight Feature Representation in Time Series Classification.*  
  arXiv preprint: [arXiv:2504.12841](https://arxiv.org/abs/2504.12841) (2025).

- **ALT Source Code**  
  GitHub repository: [github.com/Datacompintensive/ALT](https://github.com/Datacompintensive/ALT)

---

## 📦 Repository Structure

You can clone this repository using:

```bash
git clone git@github.com:Datacompintensive/WignerCamp2025.git
cd WignerCamp2025
```

### Contents

You should get familiar with the folders in this repository in the following order:

| Folder | Description |
|--------|-------------|
| [BasicProgramming](./BasicProgramming) | Contains materials and exercises on the basics of Python programming and data processing. |
| [Mathematics](./Mathematics) | Introduces key mathematical concepts for the **ALT method**, focusing on linear algebra and the **time series classification (TSC)** problem. |
| [Terminal](./Terminal) | Gives information on the most important `linux` terminal and `vim` commands. |
| [TestsAndDocumentation](./TestsAndDocumentation) | Describes the basic usage of `pytest` and introduces the **NumPy-style docstrings** for python functions. |
| [ALT_intro](./ALT_intro) | Contains introductary exercises which prepares for intorducuction of the ALT method. |
| [ALT](./ALT) | Describes the **ALT method** in detail. |

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

Materials in this repository are provided for **educational purposes**.