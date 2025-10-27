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