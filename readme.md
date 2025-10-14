# 🧮 Advanced Matrix Calculator

A comprehensive web-based matrix calculator built with Python and Streamlit that performs various matrix operations with detailed step-by-step solutions. Perfect for students, educators, and professionals working with linear algebra.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🔢 Basic Operations
- **Matrix Addition** (A + B)
- **Matrix Subtraction** (A - B)
- **Matrix Multiplication** (A × B) with step-by-step explanation
- Automatic dimension validation

### 🔄 Transpose Operations
- Matrix transpose calculation
- Property verification: (Aᵀ)ᵀ = A
- Dimension display and transformation

### 🎯 Determinant & Inverse
- Determinant calculation for square matrices
- Step-by-step inverse matrix calculation:
  - Matrix of minors
  - Matrix of cofactors with sign patterns
  - Adjugate (adjoint) matrix
  - Inverse matrix formula: A⁻¹ = (1/det(A)) × adj(A)
- Verification: A × A⁻¹ = I
- Singular matrix detection

### 📊 Advanced Properties
- **Determinant & Trace** calculation
- **Matrix Rank** computation
- **Eigenvalues & Eigenvectors** analysis
- **Matrix Properties** detection:
  - Symmetric matrices
  - Orthogonal matrices
- **Matrix Norms**:
  - Frobenius Norm
  - L1 Norm
  - L∞ Norm

### ⚡ Power & Scalar Operations
- Scalar multiplication (k × A)
- Matrix power calculation (A^n)
- Side-by-side result comparison

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/thesnak/matrix-calculator.git
cd matrix-calculator
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open in browser**
The application will automatically open in your default browser at `http://localhost:8501`

## 📦 Requirements

Create a `requirements.txt` file with:
```
streamlit>=1.28.0
numpy>=1.24.0
pandas>=2.0.0
```

## 🎮 Usage

1. **Select an Operation**: Choose from the sidebar menu:
   - Basic Operations (Add/Sub/Multiply)
   - Transpose
   - Determinant & Inverse
   - Advanced Properties
   - Power & Scalar Operations

2. **Input Matrix Dimensions**: Select the size of your matrix(ces)

3. **Enter Matrix Values**: Fill in the matrix elements using the input fields

4. **Calculate**: Click the "Calculate" button to see detailed results

5. **View Results**: See step-by-step solutions with explanations

## 📖 Examples

### Example 1: Matrix Multiplication
```python
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

Result A × B = [[19, 22],
                 [43, 50]]
```

### Example 2: Matrix Inverse
```python
A = [[4, 7],
     [2, 6]]

det(A) = 10
A⁻¹ = [[0.6, -0.7],
       [-0.2, 0.4]]
```

### Example 3: Eigenvalues
```python
A = [[3, 1],
     [1, 3]]

Eigenvalues: λ₁ = 4, λ₂ = 2
```

## 🎨 Features Highlights

- ✅ **Interactive GUI** with real-time calculations
- ✅ **Step-by-step solutions** for educational purposes
- ✅ **Dark mode support** with optimized styling
- ✅ **Error handling** for singular matrices and dimension mismatches
- ✅ **Multiple matrix sizes** support (2×2 to 5×5)
- ✅ **Property verification** for mathematical accuracy
- ✅ **Responsive design** for different screen sizes

## 🔮 Future Enhancements

Planned features for future versions:

- [ ] System of Linear Equations Solver (Ax = b)
- [ ] Matrix Decompositions (LU, QR, SVD, Cholesky)
- [ ] Import/Export functionality (CSV, Excel)
- [ ] Matrix visualizations (Heatmaps)
- [ ] Gaussian Elimination with step-by-step row operations
- [ ] Symbolic computation with fractions
- [ ] Complex number matrix support
- [ ] Batch matrix operations
- [ ] Matrix exponentiation (e^A)
- [ ] Condition number analysis

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mohamed Mahmoud**

- LinkedIn: [linkedin.com/in/mohamed-thesnak](https://linkedin.com/in/mohamed-thesnak)
- GitHub: [github.com/thesnak](https://github.com/thesnak)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [NumPy](https://numpy.org/)
- Inspired by the need for an intuitive linear algebra learning tool

## 📧 Contact

For questions, suggestions, or feedback, please:
- Open an issue on GitHub
- Connect with me on LinkedIn
- Email: [Your preferred contact email]

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star on GitHub!

---

**Made with ❤️ and Python**