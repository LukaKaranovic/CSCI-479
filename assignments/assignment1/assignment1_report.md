# Assignment 1 Report

**Author:** Luka Karanovic

**Date:** September 28, 2026

# Exploration Process

The following section outlines the details in order to replicate by exploration process. Including requirements, setup, and two tested methods for doing my data exploration:

**Environment Requirements:** Debian-compatible Linux (or any environment supporting Python 3)

---

## Submission Files Included

* **`assignment1_report.pdf`** The report that compiles the results from the data exploration and conducts the data analysis, per the assignment's requirements.
* **`assignment1.ipynb`** The main Jupyter Notebook containing the code and explanations for gathering data for the report.
* **`assignment1.py`** A Python script exported from the main Jupyter notebook that outputs results to a `.txt` file.
* **`jupyter_requirements.txt`**  A text file listing all specific Python libraries needed to run the Jupyter notebook.
* **`python_requirements.txt`**  A text file listing all specific Python libraries needed to run the Python script.

---

## Local Setup and Installation

There will be two methods for recreating my data gathering process: one with Jupyter notebooks and one with the Python script.
* Follow these steps to create an isolated Python environment and run the notebook/script: 

### 1. Install System Dependencies
  
Open a terminal and ensure your system has Python 3, pip, and virtual environment utilities installed:

```bash
sudo apt install python3-pip python3-venv python3-dev 
# Replace 'apt' with whatever package manager you use on your device.
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
2. Install the **Jupyter extension**.
3. Open `assignment_1.ipynb`.
4. Select the environment kernel (`./venv/bin/python`) in the top-right corner.
5. Run the cells in order using the "Play" arrow icon to the top left of each cell.

#### Jupyter Option B: Using the Classic Browser Interface

1. Navigate to the project root folder.
2. Launch the local Jupyter server from your terminal: Enter the command `jupyter notebook`
3. **Ctrl + click** the link generated in your terminal to open the dashboard, and select `assignment_1.ipynb`.
4. Run the cells in order using the "Play" arrow button on the top toolbar.

---

## Interpreting Output

The steps done in the program are not in the exact order of the analysis in the report. However, each attribute and its data is together in the program's output (apart from missing values). The output of the program clearly separates each attribute and outputs its data below it.

- **Both the notebook and Python script have detailed comments on what information is being gathered in each section.**
- The order of attributes analyzed in the program follows the report: categorical, then numerical that is treated as categorical, and then numerical/continuous.
- The discretization of age is done at the end of both the program and the report, and the table generated should match.
- All tables in this report have a corresponding table outputted by the program with the same column names.

# Exploration Results (Attribute Analysis)

This section analyzes each attribute in the dataset, more specifically, for each attribute it covers:

- My understanding of the semantics of this attribute
- The data item count of this attribute
- Whether there are any missing values in this attribute and the percentage of the missing values (if there are any)
- If the attribute is categorical:
	- The data type of this attribute (ordinal or nominal)
	- The cardinality (number of the unique values) of this attribute
	- The list of possible values 
	- The frequency of each value (# of appearances)
- If the attribute is numerical:
	- The range, min and max value of this attribute
	- The average value (mean) of this attribute
	- The top three most frequent values for this attribute and their corresponding frequency

---

## Categorical Attributes

These are any attributes that have a fixed set of possible values:
- *Attributes are named based off of their column names provided on row 2 of the 'Data' sheet*

---

### checking_status
**Semantic Meaning:** The status of the applicant's existing checking account (in Deutsche Marks). This column categorizes accounts based on how much money is in their checking account at the time of taking out credit.

**Data Type:** Ordinal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value:**

| Value         | Frequency |
| ------------- | --------- |
| 'no checking' | 394       |
| '<0'          | 274       |
| '0<=X<200'    | 269       |
| '>=200'       | 63        |

---

### credit_history
**Semantic Meaning:** The applicant's credit history. This column categorizes customers into groups based on their history with paying back credit/debt to the bank. It will note if customers delayed payment in the past, currently have outstanding payments, have no history, or have a good credit history.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 5

**List of all possible values and the frequency of each value:**

| Value                            | Frequency |
| -------------------------------- | --------- |
| 'existing paid'                  | 530       |
| 'critical/other existing credit' | 293       |
| 'delayed previously'             | 88        |
| 'all paid'                       | 49        |
| ' no credits/all paid'           | 40        |

---

### purpose
**Semantic Meaning:** The applicant's purpose for taking out credit from the bank.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 10

**List of all possible values and the frequency of each value:**

| Value                | Frequency |
| -------------------- | --------- |
| radio/tv             | 280       |
| 'new car'            | 234       |
| furniture/equipment  | 181       |
| 'used car'           | 103       |
| business             | 97        |
| education            | 50        |
| repairs              | 22        |
| 'domestic appliance' | 12        |
| other                | 12        |
| retraining           | 9         |

---

### savings_status
**Semantic Meaning:** The current status of the applicant's savings account (in Deutsche Marks). This column categorizes accounts based on how much money is in their savings account at the time of taking out credit.

**Data Type:** Ordinal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 5

**List of all possible values and the frequency of each value:**

| Value              | Frequency |
| ------------------ | --------- |
| '<100'             | 603       |
| 'no known savings' | 183       |
| '100<=X<500'       | 103       |
| '500<=X<1000'      | 63        |
| '>=1000'           | 48        |

---

### employment
**Semantic Meaning:** The number of years the applicant has been employed at their current job.

**Data Type:** Ordinal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 5

**List of all possible values and the frequency of each value:**

| Value      | Frequency |
| ---------- | --------- |
| '1<=X<4'   | 339       |
| '>=7'      | 253       |
| '4<=X<7'   | 174       |
| '<1'       | 172       |
| unemployed | 62        |

---

### personal_status
**Semantic Meaning:** The applicant's gender and marital status. This categorizes applicants based on their gender and whether they are single, married, divorced, separated, or widowed.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value:**

| Value                | Frequency |
| -------------------- | --------- |
| 'male single'        | 548       |
| 'female div/dep/mar' | 310       |
| 'male mar/wid'       | 92        |
| 'male div/sep'       | 50        |

---

### other_parties
**Semantic Meaning:** Whether this credit transaction is affiliated with any other debtors or guarantors (e.g. if the applicant is taking out credit with someone else, they would be a 'co-applicant'. if the applicant has a guarantor, that means there is another third party that will pay the credit if the applicant fails to). 

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 3

**List of all possible values and the frequency of each value:**

| Value          | Frequency |
| -------------- | --------- |
| none           | 907       |
| guarantor      | 52        |
| 'co applicant' | 41        |

---

### property_magnitude
**Semantic Meaning:** The highest-value tier of property or assets owned by the applicant. 

**Data Type:** Nominal (maybe ordinal if you go by value of category)

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value:**

| Value               | Frequency |
| ------------------- | --------- |
| car                 | 332       |
| 'real estate'       | 282       |
| 'life insurance'    | 232       |
| 'no known property' | 154       |

---

### other_payment_plans
**Semantic Meaning:** Shows whether the applicant currently has active loans or other financing plans with any other financial institutions or stores outside of the bank.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 3

**List of all possible values and the frequency of each value:**

| Value  | Frequency |
| ------ | --------- |
| none   | 814       |
| bank   | 139       |
| stores | 47        |

---

### housing
**Semantic Meaning:** The applicant's current home-owning status. It indicates whether the applicant owns, rents, or lives in a home 'for free'.

**Data Type:** Ordinal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 3

**List of all possible values and the frequency of each value:**

| Value      | Frequency |
| ---------- | --------- |
| own        | 713       |
| rent       | 179       |
| 'for free' | 108       |

---

### job
**Semantic Meaning:** Classifies applicants based on economic level rather than specific occupations. This column ranges from 'unskilled resident' (low economic tier) to professional tiers like 'high qualif./mgmt'.

**Data Type:** Ordinal (can be debated on the order)

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value:**

| Value                       | Frequency |
| --------------------------- | --------- |
| skilled                     | 630       |
| 'unskilled resident'        | 200       |
| 'high qualif/self emp/mgmt' | 148       |
| 'unemp/unskilled non res'   | 22        |

---

### own_telephone
**Semantic Meaning:** Whether the applicant owns a telephone or not. This lets lenders know whether they can contact the applicant remotely by telephone or not.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 2

**List of all possible values and the frequency of each value:**

| Value | Frequency |
| ----- | --------- |
| yes   | 596       |
| no    | 404       |

---

### foreign_worker
**Semantic Meaning:** Whether or not the applicant is a foreign worker living in Germany.

**Data Type:** Nominal

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 2

**List of all possible values and the frequency of each value:**

| Value | Frequency |
| ----- | --------- |
| yes   | 963       |
| no    | 37        |

---

### Credit_Risk (Target attribute)
**Semantic Meaning:** Whether the applicant defaulted on their credit or not. Here, 'good' means the applicant repaid the credit they were given on time, while 'bad' means the applicant defaulted or had delays when repaying their credit. This is what we would be trying to predict

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 2

**List of all possible values and the frequency of each value:**

| Value | Frequency |
| ----- | --------- |
| good  | 700       |
| bad   | 300       |

---

## Numerical "Categorical" Attributes

- These attributes have a numerical column but less than 6 distinct values. This means they will be treated as a categorical attribute rather than a continuous/numerical attribute as this analysis is more helpful for understanding the data.
- These attributes are all 'ordinal' as they have a numerical value to be ordered by.

---

### installment_commitment
**Semantic Meaning:** The applicant's installment rate in percentage of disposable income. Ex. if the value is 4 then the applicant will pay back 4% of their monthly income per monthly installment.

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value (ordered by frequency):**

| Value | Frequency |
| ----- | --------- |
| 4     | 476       |
| 2     | 231       |
| 3     | 157       |
| 1     | 136       |

---

### residence_since
**Semantic Meaning:** The number of years the applicant has been a resident of their current place.

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value (ordered by frequency):**

| Value | Frequency |
| ----- | --------- |
| 4     | 413       |
| 2     | 308       |
| 3     | 149       |
| 1     | 130       |

---

### existing_credits
**Semantic Meaning:** The number of existing credits the applicant has at this bank.

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value (ordered by frequency):**

| Value | Frequency |
| ----- | --------- |
| 1     | 633       |
| 2     | 333       |
| 3     | 28        |
| 4     | 6         |

---

### num_dependents
**Semantic Meaning:** Number of people the applicant is held liable to provide maintenance/care for

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Cardinality of attribute (# of unique values):** 2

**List of all possible values and the frequency of each value (ordered by frequency):**

| Value | Frequency |
| ----- | --------- |
| 1     | 845       |
| 2     | 155       |

---

## Continuous Attributes
These are any attributes that do not have a small set of possible values:
- *Attributes are named based off of their column names provided on row 2 of the 'Data' sheet*

### duration
**Semantic Meaning:** Duration of the applicant's credit agreement with the bank (in months)

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Range of Values:** 68

**Minimum Value:** 4

**Maximum Value:** 72

**Average Value (Mean):** 20.90

**The top three most frequent values for this attribute and their corresponding frequency:**

| Frequency Ranking | Value | Frequency |
| ----------------- | ----- | --------- |
| 1st               | 24    | 184       |
| 2nd               | 12    | 179       |
| 3rd               | 18    | 113       |

---

### credit_amount
**Semantic Meaning:** The amount of credit the bank is giving to the applicant.

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Range of Values:** 18174

**Minimum Value:** 250

**Maximum Value:** 18424

**Average Value (Mean):** 3271.26

**The top three most frequent values for this attribute and their corresponding frequency:**

| Frequency Ranking | Value | Frequency |
| ----------------- | ----- | --------- |
| T-1st             | 1275  | 3         |
| T-1st             | 1262  | 3         |
| T-1st             | 1478  | 3         |

---

### age (pre-discretization)
**Semantic Meaning:** The age of the applicant.

**Data Item Count:** 1000

**# of Missing Values:** 0

**% of Missing Values:** 0%

**Range of Values:** 56

**Minimum Value:** 19

**Maximum Value:** 75

**Average Value (Mean):** 35.55

**The top three most frequent values for this attribute and their corresponding frequency:**

| Frequency Ranking | Value | Frequency |
| ----------------- | ----- | --------- |
| 1st               | 27    | 51        |
| 2nd               | 26    | 50        |
| 3rd               | 23    | 48        |

---

# Discretization of 'age' attribute

## Rationale

Between the methods of equi-width, equi-depth, and info-based discretization, I chose to go with equi-width.

Here are my two main reasons:
1. Real-world semantics:
- Age naturally maps to well-defined life stages that have different economic priorities and resources. For example:
	- Young adults in their 20s are starting their careers, likely in entry-level positions and are more likely entering credit markets to afford their first car, house, etc.
	- Adults in their 30s and 40s likely have established career path, make decent money, and are looking to build a family and pay off a house.
	- Adults in their 50s-60s are earning their peak salary, have paid off a house (back in the 1980s, where this data is from, not today) but may be paying for kids
	- Adults aged 70+ get retirement funds, don't have much to pay for as kids have moved out, etc.
- Additionally, these 'age brackets' account for generational spending habits, as generations and like-minded people are grouped together.
- These 'age brackets' are also easier to interpret, as people normally group ages this way already.

2. Avoiding overfitting
- Using information-based discretization looks directly at the target variable (Credit_Risk) for this dataset to choose cutoffs. This would be better for this specific dataset, but it can easily overfit on anomalies 
	- Ex. if people aged 34-35 in this 1970s German dataset happened to have a weird spike in defaults, info-based discretization would make a strange bin. 
		- This doesn't mean 34-35 year olds don't pay off their credits, but their could have been something happening in the 70s or in Germany that made it difficult for those people to pay their credit back. Additionally, it could have just been random chance (more likely to occur here than equi-width where groupings are larger)
		- This means the model could make inaccurate predictions on the credit risk of 34-35 year olds in other places or times.
- Therefore info-based is more prone to overfitting on local patterns in training data.
- What about equi-depth? It could work, but the dataset could have a heavily skewed age demographic (say 800 adults younger than 35 and 200 above 35). This would create uneven intervals:
	- A bin for young adults may span for only 3 years (ages 24-27). While a bin for older adults may span 20 years (50-70).
- This makes it harder for humans to interpret, loses those distinct "life-stages" in each bin, and eliminates generation-based spending habits

So dividing age into uniform intervals (e.g. 10 year brackets) not only is more intuitive for humans to interpret, but it also aligns with natural demographic grouping in the real world. This makes **equi-width** the safest option.

Based on the reasons I described above, I will split the bins into 10 year intervals. To make it easier to interpret, I will start near the 'decade' marker (E.g. 19-28 instead of 16-25). Since the minimum age in the dataset is 19, and the maximum is 75, we will have these bins:
- **19–28:** Young adults / starting careers
- **29–38:** Establishing careers / family building
- **39–48:** Peak career / mid-life stability
- **49–58:** Late career / pre-retirement
- **59–68:** Traditional retirement age
- **69–78:** Post-retirement / fixed income

## Analysis

---

### age (post-discretization)

**Cardinality of attribute (# of unique values):** 4

**List of all possible values and the frequency of each value (ordered by age):**

| Age Bracket | Frequency |
| ----------- | --------- |
| 19-28       | 334       |
| 29-38       | 346       |
| 39-48       | 181       |
| 49-58       | 85        |
| 59-68       | 47        |
| 69-78       | 7         |
