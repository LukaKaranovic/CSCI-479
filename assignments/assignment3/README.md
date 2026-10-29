# Assignment Submission: Assignment 3

**Author:** Luka Karanovic

**Date:** October 28, 2026

**Environment Requirements:** Debian-compatible Linux (or any environment supporting Python 3)

---

## Submission Files Included

* **`assignment3_report.pdf`** The report that compiles the results from the data exploration, decision tree building and analysis, and decision tree testing process.
* **`assignment3.py`** A Python script containing the data preprocessing, model building, model visualization, and model testing.
  * Note: the script will generate 2 files in the directory it is executed in: a PNG for the generated decision tree and a PNG for the confusion matrix.
* **`requirements.txt`**  A text file listing all specific Python libraries needed to run the Python script.

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

* _Note: Virtual environment folders can create a lot of files which can cause you to exceed the file limit quota, so be wary._

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
3. Analyze the outputted results in `naive_bayes_confusion_matrix.png`, located in the project root folder.
