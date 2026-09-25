# Assignment Submission: Assignment 1

**Author:** Luka Karanovic

**Date:** September 23, 2026

**Environment Requirements:** Debian-compatible Linux (or any environment supporting Python 3)

---

## Submission Files Included

* **`assignment_1.ipynb`**  The main Jupyter Notebook containing the code, explanations, and final report.
* **`requirements.txt`**  A text file listing all specific Python libraries needed to run the notebook.

---

## Local Setup and Installation (Debian)

Follow these steps to create an isolated environment and run the notebook on the Debian lab machines:

### 1. Install System Dependencies

Open a terminal and ensure your system has Python 3, pip, and virtual environment utilities installed:

```bash
sudo apt install python3-pip python3-venv python3-dev
```

### 2. Set Up the Virtual Environment

**Navigate to the project root folder** and create a localized virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

* _Note: Virtual environment folders can create a lot of files which can cause you to exceed the file limit quota, so be wary._

### 3. Install Python Dependencies

Upgrade `pip` and install all required libraries exactly as specified in the submission package:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the Assignment

#### Option A: Using Visual Studio Code (Recommended)

1. Open this project folder in VS Code.
2. Install the **Jupyter extension** if prompted.
3. Open `assignment_1.ipynb`.
4. Select the environment kernel (`./venv/bin/python`) in the top-right corner and run the cells.

#### Option B: Using the Classic Browser Interface

1. Launch the local Jupyter server from your terminal: Enter the command `jupyter notebook`
2. **Ctrl + click** the link generated in your terminal to open the dashboard, and select `assignment_1.ipynb`.
