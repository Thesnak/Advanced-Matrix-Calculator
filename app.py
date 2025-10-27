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
     "Power & Scalar Operations",
     "System of Linear Equations",
     "Matrix Decompositions",
     "Import/Export Matrix"]
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
            
            st.write("**Step 2:** Interactive Matrix Multiplication Visualization")
            
            result = np.matmul(matrix_a, matrix_b)
            
            # Convert matrices to JSON for JavaScript
            import json
            matrix_a_json = json.dumps(matrix_a.tolist())
            matrix_b_json = json.dumps(matrix_b.tolist())
            result_json = json.dumps(result.tolist())
            
            # Create interactive HTML/JS visualization
            st.components.v1.html(f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: transparent;
                        margin: 0;
                        padding: 20px;
                    }}
                    .container {{
                        display: flex;
                        flex-direction: column;
                        gap: 20px;
                        align-items: center;
                    }}
                    .matrices-row {{
                        display: flex;
                        gap: 30px;
                        align-items: center;
                        justify-content: center;
                        flex-wrap: wrap;
                    }}
                    .matrix-container {{
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }}
                    .matrix-label {{
                        font-weight: bold;
                        margin-bottom: 10px;
                        font-size: 18px;
                        color: #1f77b4;
                    }}
                    table {{
                        border-collapse: collapse;
                        background: rgba(255, 255, 255, 0.05);
                        border-radius: 8px;
                        overflow: hidden;
                    }}
                    td {{
                        padding: 12px 16px;
                        text-align: center;
                        border: 1px solid rgba(128, 128, 128, 0.3);
                        min-width: 50px;
                        font-size: 16px;
                        transition: all 0.3s ease;
                    }}
                    .highlight-row {{
                        background-color: rgba(31, 119, 180, 0.4) !important;
                        transform: scale(1.05);
                        font-weight: bold;
                    }}
                    .highlight-col {{
                        background-color: rgba(255, 127, 14, 0.4) !important;
                        transform: scale(1.05);
                        font-weight: bold;
                    }}
                    .highlight-result {{
                        background-color: rgba(44, 160, 44, 0.5) !important;
                        transform: scale(1.1);
                        font-weight: bold;
                        box-shadow: 0 0 20px rgba(44, 160, 44, 0.6);
                    }}
                    .controls {{
                        display: flex;
                        gap: 10px;
                        margin: 20px 0;
                        flex-wrap: wrap;
                        justify-content: center;
                    }}
                    button {{
                        padding: 12px 24px;
                        font-size: 16px;
                        cursor: pointer;
                        border: none;
                        border-radius: 8px;
                        background: linear-gradient(135deg, #1f77b4, #1a5f8f);
                        color: white;
                        font-weight: bold;
                        transition: all 0.3s ease;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    }}
                    button:hover {{
                        transform: translateY(-2px);
                        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                        background: linear-gradient(135deg, #1a5f8f, #1f77b4);
                    }}
                    button:disabled {{
                        background: #666;
                        cursor: not-allowed;
                        transform: none;
                    }}
                    .calculation {{
                        margin: 20px 0;
                        padding: 20px;
                        background: rgba(31, 119, 180, 0.1);
                        border-radius: 8px;
                        border-left: 4px solid #1f77b4;
                        min-height: 80px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                    }}
                    .calc-title {{
                        font-weight: bold;
                        color: #1f77b4;
                        margin-bottom: 10px;
                        font-size: 18px;
                    }}
                    .calc-formula {{
                        font-family: 'Courier New', monospace;
                        font-size: 16px;
                        line-height: 1.6;
                        color: #e0e0e0;
                    }}
                    .operator {{
                        font-size: 24px;
                        color: #1f77b4;
                        font-weight: bold;
                    }}
                    .speed-control {{
                        display: flex;
                        align-items: center;
                        gap: 10px;
                    }}
                    input[type="range"] {{
                        width: 200px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="controls">
                        <button onclick="startAnimation()" id="startBtn">▶️ Start Animation</button>
                        <button onclick="pauseAnimation()" id="pauseBtn" disabled>⏸️ Pause</button>
                        <button onclick="resetAnimation()" id="resetBtn">🔄 Reset</button>
                        <button onclick="stepForward()" id="stepBtn">⏭️ Next Step</button>
                        <div class="speed-control">
                            <label>Speed:</label>
                            <input type="range" id="speedRange" min="200" max="2000" value="1000" step="100">
                            <span id="speedLabel">1.0x</span>
                        </div>
                    </div>
                    
                    <div class="calculation" id="calculation">
                        <div class="calc-title">Click "Start Animation" to see how matrix multiplication works!</div>
                        <div class="calc-formula">Each element is calculated by multiplying row elements with column elements</div>
                    </div>
                    
                    <div class="matrices-row">
                        <div class="matrix-container">
                            <div class="matrix-label">Matrix A</div>
                            <table id="matrixA"></table>
                        </div>
                        
                        <div class="operator">×</div>
                        
                        <div class="matrix-container">
                            <div class="matrix-label">Matrix B</div>
                            <table id="matrixB"></table>
                        </div>
                        
                        <div class="operator">=</div>
                        
                        <div class="matrix-container">
                            <div class="matrix-label">Result Matrix</div>
                            <table id="matrixResult"></table>
                        </div>
                    </div>
                </div>
                
                <script>
                    const matrixA = {matrix_a_json};
                    const matrixB = {matrix_b_json};
                    const result = {result_json};
                    
                    let currentRow = 0;
                    let currentCol = 0;
                    let animationInterval = null;
                    let isPaused = false;
                    let animationSpeed = 1000;
                    
                    function createMatrix(matrix, containerId) {{
                        const table = document.getElementById(containerId);
                        table.innerHTML = '';
                        matrix.forEach((row, i) => {{
                            const tr = document.createElement('tr');
                            row.forEach((cell, j) => {{
                                const td = document.createElement('td');
                                td.textContent = cell.toFixed(2);
                                td.id = `${{containerId}}_${{i}}_${{j}}`;
                                tr.appendChild(td);
                            }});
                            table.appendChild(tr);
                        }});
                    }}
                    
                    function createResultMatrix() {{
                        const table = document.getElementById('matrixResult');
                        table.innerHTML = '';
                        result.forEach((row, i) => {{
                            const tr = document.createElement('tr');
                            row.forEach((cell, j) => {{
                                const td = document.createElement('td');
                                td.textContent = '?';
                                td.id = `matrixResult_${{i}}_${{j}}`;
                                tr.appendChild(td);
                            }});
                            table.appendChild(tr);
                        }});
                    }}
                    
                    function clearHighlights() {{
                        document.querySelectorAll('td').forEach(td => {{
                            td.classList.remove('highlight-row', 'highlight-col', 'highlight-result');
                        }});
                    }}
                    
                    function calculateElement(row, col) {{
                        clearHighlights();
                        
                        // Highlight row in matrix A
                        matrixA[row].forEach((_, j) => {{
                            document.getElementById(`matrixA_${{row}}_${{j}}`).classList.add('highlight-row');
                        }});
                        
                        // Highlight column in matrix B
                        matrixB.forEach((_, i) => {{
                            document.getElementById(`matrixB_${{i}}_${{col}}`).classList.add('highlight-col');
                        }});
                        
                        // Calculate and show formula
                        let formula = `Result[${{row}}][${{col}}] = `;
                        let calculations = [];
                        let sum = 0;
                        
                        for (let k = 0; k < matrixA[row].length; k++) {{
                            const a = matrixA[row][k];
                            const b = matrixB[k][col];
                            const product = a * b;
                            sum += product;
                            calculations.push(`(${{a.toFixed(2)}} × ${{b.toFixed(2)}})`);
                        }}
                        
                        formula += calculations.join(' + ');
                        formula += ` = ${{sum.toFixed(4)}}`;
                        
                        document.getElementById('calculation').innerHTML = `
                            <div class="calc-title">Calculating Element [${{row}}][${{col}}]</div>
                            <div class="calc-formula">${{formula}}</div>
                        `;
                        
                        // Update result matrix
                        const resultCell = document.getElementById(`matrixResult_${{row}}_${{col}}`);
                        resultCell.textContent = sum.toFixed(4);
                        resultCell.classList.add('highlight-result');
                    }}
                    
                    function stepForward() {{
                        if (currentRow < result.length) {{
                            calculateElement(currentRow, currentCol);
                            
                            currentCol++;
                            if (currentCol >= result[0].length) {{
                                currentCol = 0;
                                currentRow++;
                            }}
                            
                            if (currentRow >= result.length) {{
                                document.getElementById('calculation').innerHTML = `
                                    <div class="calc-title">✅ Animation Complete!</div>
                                    <div class="calc-formula">All elements have been calculated successfully.</div>
                                `;
                                stopAnimation();
                            }}
                        }}
                    }}
                    
                    function startAnimation() {{
                        if (currentRow >= result.length) {{
                            resetAnimation();
                        }}
                        
                        document.getElementById('startBtn').disabled = true;
                        document.getElementById('pauseBtn').disabled = false;
                        document.getElementById('stepBtn').disabled = true;
                        isPaused = false;
                        
                        animationInterval = setInterval(() => {{
                            if (!isPaused) {{
                                stepForward();
                            }}
                        }}, animationSpeed);
                    }}
                    
                    function pauseAnimation() {{
                        isPaused = !isPaused;
                        document.getElementById('pauseBtn').textContent = isPaused ? '▶️ Resume' : '⏸️ Pause';
                    }}
                    
                    function stopAnimation() {{
                        clearInterval(animationInterval);
                        document.getElementById('startBtn').disabled = false;
                        document.getElementById('pauseBtn').disabled = true;
                        document.getElementById('stepBtn').disabled = false;
                    }}
                    
                    function resetAnimation() {{
                        stopAnimation();
                        currentRow = 0;
                        currentCol = 0;
                        clearHighlights();
                        createResultMatrix();
                        document.getElementById('calculation').innerHTML = `
                            <div class="calc-title">Click "Start Animation" to see how matrix multiplication works!</div>
                            <div class="calc-formula">Each element is calculated by multiplying row elements with column elements</div>
                        `;
                    }}
                    
                    // Speed control
                    document.getElementById('speedRange').addEventListener('input', (e) => {{
                        animationSpeed = parseInt(e.target.value);
                        const speed = (2200 - animationSpeed) / 1000;
                        document.getElementById('speedLabel').textContent = speed.toFixed(1) + 'x';
                        
                        if (animationInterval) {{
                            clearInterval(animationInterval);
                            if (!isPaused) {{
                                animationInterval = setInterval(() => {{
                                    if (!isPaused) {{
                                        stepForward();
                                    }}
                                }}, animationSpeed);
                            }}
                        }}
                    }});
                    
                    // Initialize
                    createMatrix(matrixA, 'matrixA');
                    createMatrix(matrixB, 'matrixB');
                    createResultMatrix();
                </script>
            </body>
            </html>
            """, height=700)
            
            st.markdown("---")
            st.write("**Final Result: A × B =**")
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

elif operation == "System of Linear Equations":
    st.header("📐 System of Linear Equations Solver (Ax = b)")
    
    st.write("Solve the system: **Ax = b**")
    
    size = st.selectbox("Number of equations/variables", [2, 3, 4, 5], index=1, key="eq_size")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("Coefficient Matrix A")
        matrix_a = []
        for i in range(size):
            row = []
            cols = st.columns(size)
            for j in range(size):
                with cols[j]:
                    val = st.number_input(f"a[{i},{j}]", value=1.0 if i == j else 0.0, 
                                         key=f"eq_a_{i}_{j}", label_visibility="collapsed")
                    row.append(val)
            matrix_a.append(row)
        matrix_a = np.array(matrix_a)
    
    with col2:
        st.subheader("Constants Vector b")
        vector_b = []
        for i in range(size):
            val = st.number_input(f"b[{i}]", value=float(i+1), 
                                 key=f"eq_b_{i}", label_visibility="collapsed")
            vector_b.append(val)
        vector_b = np.array(vector_b)
    
    method = st.radio("Solution Method:", 
                     ["Matrix Inverse", "Gaussian Elimination", "LU Decomposition"], 
                     horizontal=True)
    
    if st.button("Solve System", type="primary"):
        st.markdown("---")
        
        # Display the system
        st.subheader("System of Equations")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Matrix A:**")
            st.write(format_matrix(matrix_a))
        with col2:
            st.write("**Vector b:**")
            st.write(format_matrix(vector_b.reshape(-1, 1)))
        
        # Check if solvable
        det = np.linalg.det(matrix_a)
        rank_a = np.linalg.matrix_rank(matrix_a)
        augmented = np.column_stack([matrix_a, vector_b])
        rank_ab = np.linalg.matrix_rank(augmented)
        
        st.markdown("---")
        st.subheader("📊 System Analysis")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Determinant", f"{det:.4f}")
        with col2:
            st.metric("Rank(A)", rank_a)
        with col3:
            st.metric("Rank([A|b])", rank_ab)
        
        if abs(det) < 1e-10:
            st.error("⚠️ The system has no unique solution (det = 0)")
        elif rank_a != rank_ab:
            st.error("⚠️ The system is inconsistent (no solution)")
        else:
            st.success("✅ The system has a unique solution")
            
            st.markdown("---")
            
            if method == "Matrix Inverse":
                st.subheader("Method: Matrix Inverse (x = A⁻¹b)")
                
                st.write("**Step 1:** Calculate A⁻¹")
                try:
                    inverse_a = np.linalg.inv(matrix_a)
                    st.write(format_matrix(inverse_a))
                    
                    st.write("**Step 2:** Multiply A⁻¹ by b")
                    solution = np.dot(inverse_a, vector_b)
                    st.write("**x = A⁻¹b =**")
                    st.write(format_matrix(solution.reshape(-1, 1)))
                except:
                    st.error("Could not compute inverse")
                    solution = None
                    
            elif method == "Gaussian Elimination":
                st.subheader("Method: Gaussian Elimination")
                
                # Create augmented matrix
                aug_matrix = np.column_stack([matrix_a.copy(), vector_b.copy()])
                st.write("**Step 1:** Augmented Matrix [A|b]")
                st.write(format_matrix(aug_matrix))
                
                # Forward elimination
                n = len(aug_matrix)
                for i in range(n):
                    # Partial pivoting
                    max_row = i + np.argmax(abs(aug_matrix[i:, i]))
                    aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]
                    
                    # Make diagonal 1
                    aug_matrix[i] = aug_matrix[i] / aug_matrix[i][i]
                    
                    # Eliminate below
                    for j in range(i+1, n):
                        aug_matrix[j] = aug_matrix[j] - aug_matrix[j][i] * aug_matrix[i]
                
                st.write("**Step 2:** Row Echelon Form")
                st.write(format_matrix(aug_matrix))
                
                # Back substitution
                solution = np.zeros(n)
                for i in range(n-1, -1, -1):
                    solution[i] = aug_matrix[i][-1] - np.dot(aug_matrix[i][i+1:n], solution[i+1:])
                
                st.write("**Step 3:** Back Substitution")
                
            elif method == "LU Decomposition":
                st.subheader("Method: LU Decomposition")
                
                from scipy.linalg import lu
                P, L, U = lu(matrix_a)
                
                st.write("**Step 1:** Decompose A = PLU")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("**P (Permutation):**")
                    st.write(format_matrix(P))
                with col2:
                    st.write("**L (Lower):**")
                    st.write(format_matrix(L))
                with col3:
                    st.write("**U (Upper):**")
                    st.write(format_matrix(U))
                
                st.write("**Step 2:** Solve Ly = Pb (forward substitution)")
                Pb = np.dot(P, vector_b)
                y = np.linalg.solve(L, Pb)
                st.write(f"y = {format_matrix(y.reshape(-1, 1)).flatten()}")
                
                st.write("**Step 3:** Solve Ux = y (back substitution)")
                solution = np.linalg.solve(U, y)
            
            # Display solution
            st.markdown("---")
            st.subheader("🎯 Solution")
            if solution is not None:
                for i, val in enumerate(solution):
                    st.write(f"**x{i} = {val:.6f}**")
                
                # Verification
                st.markdown("---")
                st.subheader("✓ Verification")
                verification = np.dot(matrix_a, solution)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Ax (calculated):**")
                    st.write(format_matrix(verification.reshape(-1, 1)))
                with col2:
                    st.write("**b (expected):**")
                    st.write(format_matrix(vector_b.reshape(-1, 1)))
                
                if np.allclose(verification, vector_b):
                    st.success("✅ Solution verified: Ax = b")
                else:
                    st.warning("⚠️ Small numerical errors present")

elif operation == "Matrix Decompositions":
    st.header("🔬 Matrix Decompositions")
    
    decomp_type = st.selectbox(
        "Select Decomposition Type",
        ["LU Decomposition", "QR Decomposition", "SVD (Singular Value)", "Cholesky Decomposition"]
    )
    
    size = st.selectbox("Matrix Size", [2, 3, 4, 5], index=1, key="decomp_size")
    
    st.subheader("Input Matrix")
    matrix = []
    for i in range(size):
        row = []
        cols = st.columns(size)
        for j in range(size):
            with cols[j]:
                val = st.number_input(f"[{i},{j}]", value=1.0 if i == j else 0.0, 
                                     key=f"decomp_{i}_{j}", label_visibility="collapsed")
                row.append(val)
        matrix.append(row)
    matrix = np.array(matrix)
    
    if st.button("Decompose", type="primary"):
        st.markdown("---")
        st.header("Original Matrix A")
        st.write(format_matrix(matrix))
        
        st.markdown("---")
        
        try:
            if decomp_type == "LU Decomposition":
                st.subheader("LU Decomposition: A = PLU")
                st.write("Decomposes A into Lower and Upper triangular matrices")
                
                from scipy.linalg import lu
                P, L, U = lu(matrix)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("**P (Permutation Matrix):**")
                    st.write(format_matrix(P))
                with col2:
                    st.write("**L (Lower Triangular):**")
                    st.write(format_matrix(L))
                with col3:
                    st.write("**U (Upper Triangular):**")
                    st.write(format_matrix(U))
                
                # Verification
                st.markdown("---")
                st.subheader("✓ Verification: PLU")
                reconstruction = np.dot(P, np.dot(L, U))
                st.write(format_matrix(reconstruction))
                if np.allclose(reconstruction, matrix):
                    st.success("✅ Decomposition verified!")
                    
            elif decomp_type == "QR Decomposition":
                st.subheader("QR Decomposition: A = QR")
                st.write("Decomposes A into Orthogonal (Q) and Upper triangular (R) matrices")
                
                Q, R = np.linalg.qr(matrix)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Q (Orthogonal Matrix):**")
                    st.write(format_matrix(Q))
                    st.write("**Properties:**")
                    st.write("- Columns are orthonormal")
                    st.write("- QᵀQ = I")
                with col2:
                    st.write("**R (Upper Triangular):**")
                    st.write(format_matrix(R))
                
                # Verification
                st.markdown("---")
                st.subheader("✓ Verification")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**QR:**")
                    reconstruction = np.dot(Q, R)
                    st.write(format_matrix(reconstruction))
                with col2:
                    st.write("**QᵀQ:**")
                    qtq = np.dot(Q.T, Q)
                    st.write(format_matrix(qtq))
                
                if np.allclose(reconstruction, matrix):
                    st.success("✅ Decomposition verified!")
                    
            elif decomp_type == "SVD (Singular Value)":
                st.subheader("SVD: A = UΣVᵀ")
                st.write("Singular Value Decomposition")
                
                U, S, Vt = np.linalg.svd(matrix)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("**U (Left Singular Vectors):**")
                    st.write(format_matrix(U))
                with col2:
                    st.write("**Σ (Singular Values):**")
                    st.write(format_matrix(np.diag(S)))
                with col3:
                    st.write("**Vᵀ (Right Singular Vectors):**")
                    st.write(format_matrix(Vt))
                
                st.markdown("---")
                st.subheader("Singular Values")
                for i, s in enumerate(S):
                    st.write(f"σ{i+1} = {s:.6f}")
                
                # Verification
                st.markdown("---")
                st.subheader("✓ Verification: UΣVᵀ")
                reconstruction = np.dot(U, np.dot(np.diag(S), Vt))
                st.write(format_matrix(reconstruction))
                if np.allclose(reconstruction, matrix):
                    st.success("✅ Decomposition verified!")
                    
            elif decomp_type == "Cholesky Decomposition":
                st.subheader("Cholesky Decomposition: A = LLᵀ")
                st.write("Only for symmetric positive-definite matrices")
                
                # Check if symmetric
                if not np.allclose(matrix, matrix.T):
                    st.error("⚠️ Matrix must be symmetric for Cholesky decomposition")
                else:
                    try:
                        L = np.linalg.cholesky(matrix)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("**L (Lower Triangular):**")
                            st.write(format_matrix(L))
                        with col2:
                            st.write("**Lᵀ (Upper Triangular):**")
                            st.write(format_matrix(L.T))
                        
                        # Verification
                        st.markdown("---")
                        st.subheader("✓ Verification: LLᵀ")
                        reconstruction = np.dot(L, L.T)
                        st.write(format_matrix(reconstruction))
                        if np.allclose(reconstruction, matrix):
                            st.success("✅ Decomposition verified!")
                    except np.linalg.LinAlgError:
                        st.error("⚠️ Matrix is not positive-definite")
                        
        except Exception as e:
            st.error(f"Error during decomposition: {str(e)}")

elif operation == "Import/Export Matrix":
    st.header("📁 Import/Export Matrix")
    
    tab1, tab2 = st.tabs(["📥 Import", "📤 Export"])
    
    with tab1:
        st.subheader("Import Matrix from File")
        
        import_method = st.radio("Import Method:", ["Upload CSV/Excel", "Paste Data"], horizontal=True)
        
        if import_method == "Upload CSV/Excel":
            uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'xls'])
            
            if uploaded_file is not None:
                try:
                    if uploaded_file.name.endswith('.csv'):
                        df = pd.read_csv(uploaded_file, header=None)
                    else:
                        df = pd.read_excel(uploaded_file, header=None)
                    
                    matrix = df.values
                    st.success(f"✅ Matrix loaded successfully! Shape: {matrix.shape}")
                    
                    st.write("**Imported Matrix:**")
                    st.write(format_matrix(matrix))
                    
                    # Basic operations on imported matrix
                    st.markdown("---")
                    st.subheader("Quick Analysis")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Rows", matrix.shape[0])
                    with col2:
                        st.metric("Columns", matrix.shape[1])
                    with col3:
                        if matrix.shape[0] == matrix.shape[1]:
                            det = np.linalg.det(matrix)
                            st.metric("Determinant", f"{det:.4f}")
                        else:
                            st.metric("Type", "Non-square")
                    
                except Exception as e:
                    st.error(f"Error reading file: {str(e)}")
        
        else:  # Paste Data
            st.write("Paste matrix data (comma or space separated):")
            pasted_data = st.text_area("Matrix Data", height=200, 
                                       placeholder="1, 2, 3\n4, 5, 6\n7, 8, 9")
            
            if st.button("Load Matrix"):
                try:
                    # Try comma separated first
                    if ',' in pasted_data:
                        rows = [list(map(float, line.split(','))) for line in pasted_data.strip().split('\n')]
                    else:
                        rows = [list(map(float, line.split())) for line in pasted_data.strip().split('\n')]
                    
                    matrix = np.array(rows)
                    st.success(f"✅ Matrix loaded! Shape: {matrix.shape}")
                    st.write(format_matrix(matrix))
                    
                except Exception as e:
                    st.error(f"Error parsing data: {str(e)}")
    
    with tab2:
        st.subheader("Export Matrix to File")
        
        # Let user create a matrix to export
        export_size_rows = st.number_input("Rows", min_value=2, max_value=10, value=3, key="exp_rows")
        export_size_cols = st.number_input("Columns", min_value=2, max_value=10, value=3, key="exp_cols")
        
        st.write("**Matrix to Export:**")
        export_matrix = []
        for i in range(export_size_rows):
            row = []
            cols = st.columns(export_size_cols)
            for j in range(export_size_cols):
                with cols[j]:
                    val = st.number_input(f"[{i},{j}]", value=float(i * export_size_cols + j + 1), 
                                         key=f"exp_{i}_{j}", label_visibility="collapsed")
                    row.append(val)
            export_matrix.append(row)
        export_matrix = np.array(export_matrix)
        
        st.write(format_matrix(export_matrix))
        
        # Export options
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Export as CSV")
            csv_data = pd.DataFrame(export_matrix).to_csv(index=False, header=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv_data,
                file_name="matrix.csv",
                mime="text/csv"
            )
        
        with col2:
            st.subheader("Export as Text")
            text_data = '\n'.join(['\t'.join(map(str, row)) for row in export_matrix])
            st.download_button(
                label="📥 Download TXT",
                data=text_data,
                file_name="matrix.txt",
                mime="text/plain"
            )

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