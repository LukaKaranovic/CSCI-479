# Assignment Submission: Assignment 4

**Author:** Luka Karanovic

**Date:** November 12, 2026

**Environment Requirements:** Debian-compatible Linux (or any environment supporting Python 3)

---

## Submission Files Included

* **`assignment4_report.pdf`** The report that compiles the results from the data exploration, model training and analysis, best model results, and overall understanding of error based learning.
* **`assignment4.py`** A Python program containing the data preprocessing, model building, training visualization, and model/training results.
  * Note: the script will generate a subdirectory from the root of the project named `graphs/` that contains 10 graphs showing the error trend for each training run in a `.png` file format.
* **`requirements.txt`**  A text file listing all specific Python libraries needed to run the Python program.

---

## Local Setup and Installation

* Follow these steps to create an isolated Python environment and run the script:

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

* _Note: Virtual environment folders can create a lot of files which can cause you to exceed the file limit quota on the VIU CSCI servers, so be wary._

### 3. Install Python Dependencies

Upgrade `pip` and install all required libraries exactly as specified in the submission package:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch the Assignment

#### Python Script

1. Navigate to the project root folder.
2. Run the script by typing `python3 assignment3.py` in the terminal.
    * _If `python3` doesn't work, try replacing it with `py` or `python`_
3. Analyze the outputted results in the terminal and in the `graphs/` subdirectory, located in the project root folder.
