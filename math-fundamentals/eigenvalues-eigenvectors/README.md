
# 📐 Eigenvalues & Eigenvectors — From Scratch

## 🎯 Objective

To understand eigenvalues and eigenvectors geometrically and mathematically, solve eigenvalue problems by hand, and verify the results using Python and NumPy.

This project is part of my [Machine Learning Foundations](../../) repository.

## 📚 Concepts Covered

- Geometric interpretation of eigenvalues and eigenvectors
- Characteristic polynomial and characteristic equation
- Eigenvalue and eigenvector calculations
- Matrix trace and determinant verification
- Upper triangular matrices
- Back substitution, pivots, and free variables
- Eigenvector normalisation (L2 norm)
- Numerical precision using `np.allclose()`

## 🧮 Mathematical Foundation

An eigenvector is a nonzero vector that satisfies:

**Av = λv**

Where:
- **A** represents a square matrix.
- **v** represents an eigenvector.
- **λ** represents its corresponding eigenvalue.

The eigenvalues are obtained using the characteristic equation:

**det(A − λI) = 0**

To verify the eigenvalues:

- **Trace:** Sum of the eigenvalues equals the sum of the diagonal elements.
- **Determinant:** Product of the eigenvalues equals the determinant of the matrix.

## ✍️ Handwritten Solutions

I solved three 2×2 matrices and one 3×3 upper triangular matrix by hand.

The exercises include finding eigenvalues and eigenvectors and verifying results using trace and determinant.

<details>
<summary><strong>Problem 1 — 2×2 Diagonal Matrix</strong></summary>

![Problem 1](handwritten-solutions/problem-01.jpg)

</details>

<details>
<summary><strong>Problem 2 — 2×2 Symmetric Matrix</strong></summary>

![Problem 2](handwritten-solutions/problem-02.jpg)

</details>

<details>
<summary><strong>Problem 3 — 2×2 Symmetric Matrix</strong></summary>

![Problem 3](handwritten-solutions/problem-03.jpg)

</details>

<details>
<summary><strong>Problem 4 — 3×3 Upper Triangular Matrix</strong></summary>

![3×3 Triangular Matrix](handwritten-solutions/triangular-3x3.jpg)

</details>

## 💻 Python Implementation

📂 [View Python Implementation](eigen_verification.py)

The handwritten results were verified using NumPy.

### `np.linalg.eig()`

Used for general square matrices, including the nonsymmetric 3×3 upper triangular matrix.

### `np.linalg.eigh()`

Used for real symmetric matrices. It returns real eigenvalues and orthonormal eigenvectors.

### Numerical Verification

Each eigenpair was checked using:

**Av ≈ λv**

The implementation uses:

- `@` for matrix–vector multiplication
- `*` for scalar–vector multiplication
- `np.allclose()` for floating-point comparisons
- Loops to reduce repetitive code (DRY principle)

**Result:** All four numerical eigenpair checks passed.

## 📂 Project Structure

```text
eigenvalues-eigenvectors/
├── README.md
├── eigen_verification.py
└── handwritten-solutions/
    ├── problem-01.jpg
    ├── problem-02.jpg
    ├── problem-03.jpg
    └── triangular-3x3.jpg
```

## 🚀 How to Run

From the project folder:

```bash
python -m pip install numpy
python eigen_verification.py
```

## ✅ Key Learning Outcomes

- Understood the geometric meaning of eigenvectors and eigenvalues.
- Derived characteristic polynomials and solved eigenvalue problems manually.
- Practised identifying pivots and free variables in linear systems.
- Verified handwritten solutions using NumPy.
- Applied floating-point tolerance and the DRY principle in Python.

---

**Part of my ongoing Machine Learning Engineering learning journey — understanding the mathematics before relying on libraries.**
