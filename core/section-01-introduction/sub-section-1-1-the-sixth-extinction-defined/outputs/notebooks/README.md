<!--
✒ Metadata
    - Title: Notebook Execution Guide (SME Edition - v1.0)
    - File Name: README.md
    - Relative Path: core/section-01-introduction/sub-section-1-1-the-sixth-extinction-defined/outputs/notebooks/README.md
    - Artifact Type: docs / instructions
    - Version: 1.0.0
    - Date: 2026-01-09
    - Update: Friday, January 09, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Google - Gemini 2.0 Flash
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    User-friendly instructions for setting up the environment and executing the
    Jupyter Notebooks contained in this subsection. Designed for both technical
    users and absolute beginners.

✒ Key Features:
    - Feature 1: Step-by-step environment setup (Python/Pip)
    - Feature 2: Explanation of Validation vs. Exploratory notebooks
    - Feature 3: Troubleshooting common path issues
    - Feature 4: "One-click" execution via VS Code or Jupyter Lab

✒ Usage Instructions:
    Read this guide before attempting to run any .ipynb files in this directory.
---------
-->

# 📓 How to Run These Notebooks

Welcome! If you're looking to verify the science behind the Sixth Mass Extinction Project, you've come to the right place. These notebooks are designed to be "self-contained," meaning everything they need to run is included in this folder.

## 🚀 Quick Start (For Beginners)

### 1. Install Python
If you don't have Python yet, download it from [python.org](https://www.python.org/downloads/). Make sure to check the box that says **"Add Python to PATH"** during installation.

### 2. Open this folder in VS Code
We recommend using [Visual Studio Code](https://code.visualstudio.com/). 
1. Open VS Code.
2. Go to `File > Open Folder` and select this `notebooks/` directory.
3. Install the **Python** and **Jupyter** extensions (VS Code will usually prompt you to do this).

### 3. Install the "Kitchen Sink"
Open your terminal (in VS Code, press ``Ctrl + ` ``) and paste this command to install all the tools we use for data analysis:

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run the Notebook
1. Click on a file ending in `.ipynb` (e.g., `1.1_validate_current_vertebrate_rates.ipynb`).
2. Click the **"Run All"** button at the top of the editor.
3. If prompted to select a "Kernel," choose the Python version you just installed.

---

## 🏗️ What's Inside?

### ✅ Validation Notebooks
These reproduce established scientific claims (like the "100x" faster rate). They are the "Audit Trail" for our project.

### 🧪 Exploratory Notebooks
These look for new patterns or projections. They are where we "stress-test" the data.

---

## 🛠️ Troubleshooting

### "File Not Found" Errors
We use **Relative Paths**. This means the notebook expects to see a folder called `data/` in the same directory as itself. If you move the notebook file without moving the `data/` folder, it will break.

### "Module Not Found" Errors
If you see an error like `ModuleNotFoundError: No module named 'pandas'`, it means Step 3 above didn't finish or you are using a different version of Python than the one where you installed the tools.

---

> **Note:** All data used here is a localized copy of the raw source found in `core/grab-bag/`. This ensures that even if the global project data changes, these notebooks remain functional and auditable.
