# Assignment Submission: Assignment 1

**Author:** Luka Karanovic

**Date:** September 28, 2026

**Environment Requirements:** Debian-compatible Linux (or any environment supporting Python 3)

---

## Submission Files Included

* **`assignment1_report.pdf`** The report that compiles the results from the data exploration and conducts the data analysis, per. the assignment's requirements.
* **`assignment1.ipynb`** The main Jupyter Notebook containing the code and explanations for gathering data for the report.
* **`assignment1.py`** A Python script exported from the main Jupyter notebook that outputs results to a `.txt` file.
* **`jupyter_requirements.txt`**  A text file listing all specific Python libraries needed to run the Jupyter notebook.
* **`python_requirements.txt`**  A text file listing all specific Python libraries needed to run the Python script.

---

## Local Setup and Installation

There will be two methods for recreating my data gathering process: one with Jupyter notebooks and one with the Python script.

* Follow these steps to create an isolated Python environment and run the notebook/script:

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
# If you are running the Python script, run:
pip install -r python_requirements.txt
# If you are running the Jupyter notebook, run:
pip install -r jupyter_requirements.txt
```

### 4. Launch the Assignment

#### Python Script

1. Navigate to the project root folder.
2. Run the script by typing `python3 assignment1.py` in the terminal.
    * _If `python3` doesn't work, try replacing it with `py` or `python`_
3. Analyze the outputted results in `eda_results.txt`, located in the project root folder.

#### Jupyter Option A: Using Visual Studio Code (Recommended)

1. Open the project root folder in VS Code.
2. Install the **Jupyter extension** if prompted.
3. Open `assignment_1.ipynb`.
4. Select the environment kernel (`./venv/bin/python`) in the top-right corner and run the cells.

#### Jupyter Option B: Using the Classic Browser Interface

1. Navigate to the project root folder.
2. Launch the local Jupyter server from your terminal: Enter the command `jupyter notebook`
3. **Ctrl + click** the link generated in your terminal to open the dashboard, and select `assignment_1.ipynb`.
