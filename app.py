import streamlit as st
import numpy as np
import pandas as pd

def matrix_of_minors(matrix):
    """Calculate the matrix of minors"""
    n = len(matrix)
    minors = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            minors[i][j] = np.linalg.det(sub_matrix)
    
    return minors

def matrix_of_cofactors(minors):
    """Calculate the matrix of cofactors from minors"""
    n = len(minors)
    cofactors = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            cofactors[i][j] = minors[i][j] * ((-1) ** (i + j))
    
    return cofactors

def format_matrix(matrix):
    """Format matrix for display"""
    return np.array([[round(x, 4) for x in row] for row in matrix])

def calculate_rank(matrix):
    """Calculate the rank of a matrix"""
    return np.linalg.matrix_rank(matrix)

def calculate_trace(matrix):
    """Calculate the trace of a matrix"""
    return np.trace(matrix)

def get_eigenvalues_eigenvectors(matrix):
    """Calculate eigenvalues and eigenvectors"""
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

st.set_page_config(page_title="Matrix Calculator Pro", layout="wide", page_icon="🧮")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
    }
    .author-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: rgba(31, 119, 180, 0.1);
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
    }
    .author-box a {
        color: #58a6ff;
        text-decoration: none;
    }
    .author-box a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🧮 Advanced Matrix Calculator</h1>', unsafe_allow_html=True)
st.write("Perform comprehensive matrix operations with detailed step-by-step solutions")

# Author Information
st.markdown("""
<div class="author-box">
    <p style="margin: 0; font-size: 0.9rem;">
        <strong>👨‍💻 Author:</strong> Mohamed Mahmoud<br>
        <strong>🔗 LinkedIn:</strong> <a href="https://linkedin.com/in/mohamed-thesnak" target="_blank">linkedin.com/in/mohamed-thesnak</a><br>
        <strong>💻 GitHub:</strong> <a href="https://github.com/thesnak" target="_blank">github.com/thesnak</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar for operation selection
st.sidebar.header("⚙️ Operation Selection")
operation = st.sidebar.selectbox(
    "Choose Operation",
    ["Basic Operations (Add/Sub/Multiply)", 
     "Transpose", 
     "Determinant & Inverse",
     "Advanced Properties",
     "Power & Scalar Operations"]
)

st.sidebar.markdown("---")

# Matrix input based on operation
if operation == "Basic Operations (Add/Sub/Multiply)":
    st.header("🔢 Basic Matrix Operations")
    
    op_type = st.radio("Select Operation:", ["Addition", "Subtraction", "Multiplication"], horizontal=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Matrix A")
        rows_a = st.number_input("Rows for A", min_value=2, max_value=5, value=3, key="rows_a")
        cols_a = st.number_input("Columns for A", min_value=2, max_value=5, value=3, key="cols_a")
        
        matrix_a = []
        for i in range(rows_a):
            row = []
            cols = st.columns(cols_a)
            for j in range(cols_a):
                with cols[j]:
                    val = st.number_input(f"A[{i},{j}]", value=1.0 if i == j else 0.0, 
                                         key=f"a_{i}_{j}", label_visibility="collapsed")
                    row.append(val)
            matrix_a.append(row)
        matrix_a = np.array(matrix_a)
    
    with col2:
        st.subheader("Matrix B")
        if op_type in ["Addition", "Subtraction"]:
            rows_b = rows_a
            cols_b = cols_a
            st.info(f"Matrix B must be {rows_a}×{cols_a} for {op_type.lower()}")
        else:
            rows_b = cols_a
            cols_b = st.number_input("Columns for B", min_value=2, max_value=5, value=3, key="cols_b")
            st.info(f"Matrix B must have {cols_a} rows for multiplication")
        
        matrix_b = []
        for i in range(rows_b):
            row = []
            cols = st.columns(cols_b)
            for j in range(cols_b):
                with cols[j]:
                    val = st.number_input(f"B[{i},{j}]", value=1.0 if i == j else 0.0, 
                                         key=f"b_{i}_{j}", label_visibility="collapsed")
                    row.append(val)
            matrix_b.append(row)
        matrix_b = np.array(matrix_b)
    
    if st.button("Calculate", type="primary", key="calc_basic"):
        st.markdown("---")
        st.subheader("📊 Input Matrices")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Matrix A:**")
            st.write(format_matrix(matrix_a))
        with col2:
            st.write("**Matrix B:**")
            st.write(format_matrix(matrix_b))
        
        st.markdown("---")
        st.subheader("✨ Result")
        
        if op_type == "Addition":
            result = matrix_a + matrix_b
            st.write("**A + B =**")
            st.write(format_matrix(result))
            st.success("✅ Addition completed successfully!")
            
        elif op_type == "Subtraction":
            result = matrix_a - matrix_b
            st.write("**A - B =**")
            st.write(format_matrix(result))
            st.success("✅ Subtraction completed successfully!")
            
        elif op_type == "Multiplication":
            st.write("**Step 1:** Verify dimensions")
            st.write(f"A is {matrix_a.shape[0]}×{matrix_a.shape[1]}, B is {matrix_b.shape[0]}×{matrix_b.shape[1]}")
            st.write(f"Result will be {matrix_a.shape[0]}×{matrix_b.shape[1]}")
            
            st.write("**Step 2:** Calculate A × B")
            st.write("Each element [i,j] = sum of (row i of A) × (column j of B)")
            
            result = np.matmul(matrix_a, matrix_b)
            st.write("**A × B =**")
            st.write(format_matrix(result))
            st.success("✅ Multiplication completed successfully!")

elif operation == "Transpose":
    st.header("🔄 Matrix Transpose")
    
    st.subheader("Input Matrix")
    rows = st.number_input("Rows", min_value=2, max_value=5, value=3, key="t_rows")
    cols = st.number_input("Columns", min_value=2, max_value=5, value=3, key="t_cols")
    
    matrix = []
    for i in range(rows):
        row = []
        columns = st.columns(cols)
        for j in range(cols):
            with columns[j]:
                val = st.number_input(f"[{i},{j}]", value=float(i * cols + j + 1), 
                                     key=f"t_{i}_{j}", label_visibility="collapsed")
                row.append(val)
        matrix.append(row)
    matrix = np.array(matrix)
    
    if st.button("Calculate Transpose", type="primary"):
        st.markdown("---")
        st.subheader("Original Matrix A")
        st.write(f"Dimensions: {rows}×{cols}")
        st.write(format_matrix(matrix))
        
        st.subheader("Transposed Matrix Aᵀ")
        st.write(f"Dimensions: {cols}×{rows}")
        st.write("The transpose swaps rows and columns: Aᵀ[i,j] = A[j,i]")
        transpose = matrix.T
        st.write(format_matrix(transpose))
        
        st.success("✅ Transpose completed!")
        
        # Properties
        st.info("**Property Check:** (Aᵀ)ᵀ = A")
        double_transpose = transpose.T
        if np.allclose(double_transpose, matrix):
            st.write("✓ Verified: Transposing twice returns the original matrix")

elif operation == "Determinant & Inverse":
    st.header("🔢 Determinant & Inverse Matrix")
    
    size = st.selectbox("Matrix Size (must be square)", [2, 3, 4], index=1)
    
    st.subheader("Input Matrix")
    matrix = []
    for i in range(size):
        row = []
        cols = st.columns(size)
        for j in range(size):
            with cols[j]:
                val = st.number_input(f"[{i},{j}]", value=1.0 if i == j else 0.0, 
                                     key=f"inv_{i}_{j}", label_visibility="collapsed")
                row.append(val)
        matrix.append(row)
    matrix = np.array(matrix)
    
    if st.button("Calculate", type="primary", key="calc_inv"):
        st.markdown("---")
        st.header("Original Matrix A")
        st.write(format_matrix(matrix))
        
        # Calculate determinant
        det = np.linalg.det(matrix)
        
        st.header("Step 1: Calculate Determinant")
        st.write(f"**det(A) = {det:.4f}**")
        
        if abs(det) < 1e-10:
            st.error("⚠️ The matrix is singular (determinant = 0). The inverse does not exist!")
        else:
            # Matrix of Minors
            st.header("Step 2: Calculate Matrix of Minors")
            st.write("For each element, find the determinant of the submatrix:")
            minors = matrix_of_minors(matrix)
            st.write(format_matrix(minors))
            
            # Matrix of Cofactors
            st.header("Step 3: Calculate Matrix of Cofactors")
            sign_pattern = [[((-1) ** (i + j)) for j in range(size)] for i in range(size)]
            st.write("**Sign Pattern:**")
            st.write(np.array(sign_pattern))
            
            cofactors = matrix_of_cofactors(minors)
            st.write("**Matrix of Cofactors:**")
            st.write(format_matrix(cofactors))
            
            # Adjugate
            st.header("Step 4: Calculate Adjugate Matrix")
            adjugate = cofactors.T
            st.write("**adj(A) = Cᵀ**")
            st.write(format_matrix(adjugate))
            
            # Inverse
            st.header("Step 5: Calculate Inverse Matrix")
            st.write(f"**A⁻¹ = (1/{det:.4f}) × adj(A)**")
            inverse = adjugate / det
            st.write(format_matrix(inverse))
            
            # Verification
            st.header("✓ Verification")
            verification = np.matmul(matrix, inverse)
            st.write("**A × A⁻¹ =**")
            st.write(format_matrix(verification))
            
            if np.allclose(verification, np.eye(size)):
                st.success("✅ Perfect! The inverse is correct.")

elif operation == "Advanced Properties":
    st.header("📐 Advanced Matrix Properties")
    
    size = st.selectbox("Matrix Size (square)", [2, 3, 4], index=1, key="adv_size")
    
    st.subheader("Input Matrix")
    matrix = []
    for i in range(size):
        row = []
        cols = st.columns(size)
        for j in range(size):
            with cols[j]:
                val = st.number_input(f"[{i},{j}]", value=1.0 if i == j else 0.0, 
                                     key=f"adv_{i}_{j}", label_visibility="collapsed")
                row.append(val)
        matrix.append(row)
    matrix = np.array(matrix)
    
    if st.button("Analyze Matrix", type="primary"):
        st.markdown("---")
        st.header("Matrix A")
        st.write(format_matrix(matrix))
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Basic Properties")
            det = np.linalg.det(matrix)
            st.write(f"**Determinant:** {det:.4f}")
            
            trace = calculate_trace(matrix)
            st.write(f"**Trace (sum of diagonal):** {trace:.4f}")
            
            rank = calculate_rank(matrix)
            st.write(f"**Rank:** {rank}")
            
            # Check if symmetric
            is_symmetric = np.allclose(matrix, matrix.T)
            st.write(f"**Symmetric:** {'Yes' if is_symmetric else 'No'}")
            
            # Check if orthogonal
            is_orthogonal = np.allclose(np.matmul(matrix, matrix.T), np.eye(size))
            st.write(f"**Orthogonal:** {'Yes' if is_orthogonal else 'No'}")
        
        with col2:
            st.subheader("🎯 Eigenvalues & Eigenvectors")
            try:
                eigenvalues, eigenvectors = get_eigenvalues_eigenvectors(matrix)
                st.write("**Eigenvalues:**")
                for i, ev in enumerate(eigenvalues):
                    if np.isreal(ev):
                        st.write(f"λ{i+1} = {np.real(ev):.4f}")
                    else:
                        st.write(f"λ{i+1} = {ev:.4f}")
                
                st.write("**Eigenvectors:**")
                st.write(format_matrix(np.real(eigenvectors)))
            except:
                st.warning("Could not compute eigenvalues/eigenvectors")
        
        st.markdown("---")
        st.subheader("🔍 Matrix Norms")
        col1, col2, col3 = st.columns(3)
        with col1:
            frobenius_norm = np.linalg.norm(matrix, 'fro')
            st.metric("Frobenius Norm", f"{frobenius_norm:.4f}")
        with col2:
            l1_norm = np.linalg.norm(matrix, 1)
            st.metric("L1 Norm", f"{l1_norm:.4f}")
        with col3:
            linf_norm = np.linalg.norm(matrix, np.inf)
            st.metric("L∞ Norm", f"{linf_norm:.4f}")

elif operation == "Power & Scalar Operations":
    st.header("⚡ Power & Scalar Operations")
    
    size = st.selectbox("Matrix Size", [2, 3, 4], index=1, key="pow_size")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Input Matrix")
        matrix = []
        for i in range(size):
            row = []
            cols = st.columns(size)
            for j in range(size):
                with cols[j]:
                    val = st.number_input(f"[{i},{j}]", value=1.0 if i == j else 0.0, 
                                         key=f"pow_{i}_{j}", label_visibility="collapsed")
                    row.append(val)
            matrix.append(row)
        matrix = np.array(matrix)
    
    with col2:
        st.subheader("Operations")
        scalar = st.number_input("Scalar value (k)", value=2.0)
        power = st.number_input("Power (n)", min_value=1, max_value=10, value=2)
    
    if st.button("Calculate", type="primary", key="calc_pow"):
        st.markdown("---")
        st.header("Original Matrix A")
        st.write(format_matrix(matrix))
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Scalar Multiplication")
            st.write(f"**k × A where k = {scalar}**")
            scalar_result = scalar * matrix
            st.write(format_matrix(scalar_result))
        
        with col2:
            st.subheader("Matrix Power")
            st.write(f"**A^{power}** (A multiplied by itself {power} times)")
            power_result = np.linalg.matrix_power(matrix, power)
            st.write(format_matrix(power_result))

# Examples and Help
st.sidebar.markdown("---")
st.sidebar.header("📚 Quick Help")

with st.sidebar.expander("💡 Tips"):
    st.write("""
    - Use **Basic Operations** for A+B, A-B, A×B
    - **Transpose** swaps rows and columns
    - **Determinant & Inverse** for square matrices
    - **Advanced Properties** shows eigenvalues, rank, trace
    - **Power Operations** for A^n and scalar multiplication
    """)

with st.sidebar.expander("🎓 Recommendations"):
    st.write("""
    **Study Suggestions:**
    1. Start with 2×2 matrices to understand concepts
    2. Try identity matrices to verify properties
    3. Experiment with symmetric matrices
    4. Check if A × A⁻¹ = I always holds
    5. Compare eigenvalues with trace and determinant
    
    **Advanced Features:**
    - Matrix decompositions (LU, QR, SVD)
    - System of equations solver
    - Matrix exponentiation
    - Condition number analysis
    """)

st.sidebar.info("💾 **Pro Tip:** Take screenshots of results for your notes!")