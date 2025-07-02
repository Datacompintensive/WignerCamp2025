# WignerCamp2025

This repository contains the educational materials for the **2025 Wigner Summer Camp** organized by the **Data and Compute Intensive Sciences Research Group** at the Wigner Research Centre for Physics.

The camp is designed for high school students and introduces the mathematical and computational foundations of **time series classification**, culminating in practical sessions using the **ALT method**.

---

## ⏰ Recommended timeline

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable</title>
</head>
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
            <td class="time-column">9:00-9:15</td>
            <td rowspan="2">Opening Ceremony</td>
            <td rowspan="8">Basic Programming II²</td>
            <td></td>
            <td></td>
            <td rowspan="6">Creating presentation</td>
        </tr>
        <tr>
            <td class="time-column">9:15-9:30</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">9:30-9:45</td>
            <td rowspan="2">Introduction</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">9:45-10:00</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">10:00-10:15</td>
            <td rowspan="6">Introduction to Linear Algebra</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">10:15-10:30</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">10:30-10:45</td>
            <td></td>
            <td></td>
            <td rowspan="4">Finalizing presentation</td>
        </tr>
        <tr>
            <td class="time-column">10:45-11:00</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">11:00-11:15</td>
            <td rowspan="6">ALT introduction - Eigenvectors</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">11:15-11:30</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">11:30-11:45</td>
            <td>Revision, short test</td>
            <td></td>
            <td></td>
            <td rowspan="4">Presentation practice</td>
        </tr>
        <tr>
            <td class="time-column">11:45-12:00</td>
            <td rowspan="3">Mathematical foundations of TSC</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">12:00-12:15</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">12:15-12:30</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">12:30-12:45</td>
            <td rowspan="3">Lunch</td>
            <td rowspan="3">Lunch</td>
            <td rowspan="3">Lunch</td>
            <td rowspan="3">Lunch</td>
            <td rowspan="3">Lunch</td>
        </tr>
        <tr>
            <td class="time-column">12:45-13:00</td>
        </tr>
        <tr>
            <td class="time-column">13:00-13:15</td>
        </tr>
        <tr>
            <td class="time-column">13:15-13:30</td>
            <td>Introduction to VIM</td>
            <td rowspan="5">ALT introduction - Feature extraction</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">13:30-13:45</td>
            <td rowspan="4">Basic Programming I¹</td>
            <td rowspan="10">Non project related activity (visiting nuclear reactor)</td>
            <td></td>
            <td  rowspan="10">Closing & presentation</td>
        </tr>
        <tr>
            <td class="time-column">13:45-14:00</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">14:00-14:15</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">14:15-14:30</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">14:30-14:45</td>
            <td rowspan="6">Computing Exercises</td>
            <td rowspan="6">The Method - Adaptive Law-based Transformation</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">14:45-15:00</td>
            <td></td>
        <tr>
            <td class="time-column">15:00-15:15</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">15:15-15:30</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">15:30-15:45</td>
            <td></td>
        </tr>
        <tr>
            <td class="time-column">15:45-16:00</td>
            <td></td>
        </tr>
    </table>
</body>
</html>

¹ *Basic Programming I* includes the modules based on the need of the *Computing Exercises* - Python, Pytorch and Pandas.

² *Basic Programming II* includes Numpy and Matplotlib.

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