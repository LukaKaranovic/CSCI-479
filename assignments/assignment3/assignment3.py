import pandas as pd
import numpy as np

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# ================================
# DATA IMPORT AND PREPROCESSING
# ================================

# We load the training data from the specific 'Training Dataset' sheet from the Excel file 
    # Metadata/title rows at the top are skipped using skiprows
    # Only the columns we care about (that contain information) are loaded using usecols
train_df = pd.read_excel(
    'GermanCredit_Dataset_modified.xlsx',
    sheet_name='Training Dataset',      
    skiprows=1,             
    usecols='B:G',
    header=0      
)

# Get the testing data from 'testing dataset' sheet
test_df = pd.read_excel(
    'GermanCredit_Dataset_modified.xlsx',
    sheet_name='Testing Dataset',      
    skiprows=1,             
    usecols='B:G',
    header=0        
)

features = ['purpose', 'employment', 'housing', 'job', 'foreign_worker']
target = 'Credit_Risk'

# Print the string names found in the first row (headers) to confirm all columns were loaded correctly
print("Loaded columns:", train_df.columns.tolist())

# Separate descriptive features (X) and target (y) for both sets
X_train_raw = train_df[features]
y_train = train_df[target]

X_test_raw = test_df[features]
y_test = test_df[target]


# === NOTE ===
# Scikit-learn's categorical Naive Bayes algorithm cannot process raw text strings and will throw a ValueError if you try to pass text directly.
# Therefore we must convert categorical attributes to numerical. 
# We will use Scikit-learn's OrdinalEncoder (map each category to a distinct non-negative integer).
encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)

# Combine train and test datasets before Ordinal Encoding 
# This guarantees both sets have the exact same 'category to integer' mapping.
combined_X = pd.concat([X_train_raw, X_test_raw], axis=0)
encoder.fit(combined_X)

# ==========================================
# TRAIN THE MODEL
# ==========================================

# Apply ordinal encoding: swap category strings for their corresponding ints
    # e.g. 'employed' -> 1
X_train = pd.DataFrame(encoder.transform(X_train_raw), columns=features)
X_test = pd.DataFrame(encoder.transform(X_test_raw), columns=features)

# Train Categorical Naive Bayes Classifier
nb_classifier = CategoricalNB()
nb_classifier.fit(X_train, y_train)

# ==========================================
# DISPLAY CALCULATED PROBABILITIES
# ==========================================
print("=== CATEGORICAL NAIVE BAYES PROBABILITIES ===")



# Prior Probabilities P(Y)
    # Why use logs? Computer implementations of Naive Bayes commonly store probabilities in "log-space" 
    # (using natural logarithms, ln). This is because multiplying many tiny probabilities together 
    # can cause computer floating-point numbers to "underflow" (crash to zero). Adding logarithms avoids this.

# Convert log-probabilities back to standard decimals (0 to 1) by applying exponential function (np.exp, which calculates e^x).
class_priors = np.exp(nb_classifier.class_log_prior_)

print(f"Classes found: {nb_classifier.classes_}")
print("Prior Probabilities P(Y):")
for c_label, prior in zip(nb_classifier.classes_, class_priors):
    print(f"  P(Credit_Risk = {c_label}) = {prior:.3f}")

# Category Likelihoods P(X_i = category | Class)
    # nb_classifier.category_log_prob_ is a list of arrays (one array per feature).
    # Each array stores the log-likelihood of every possible category for that feature, given each class: ln(P(Feature_i = category | Class)).
    # Under the hood, scikit-learn also applies Laplacian smoothing to ensure a probability of zero never wipes out all other calculations.
print("\nCategory Likelihoods P(Feature = Category | Class):")
for idx, feature_name in enumerate(features):
    print(f"\nFeature: '{feature_name}'")
    categories = encoder.categories_[idx]
    # category_log_prob_[idx] holds the log probabilities for each category of this feature
    log_probs = nb_classifier.feature_log_prob_[idx]

    # Loop through each target class ('Bad' and 'Good')
    for c_idx, c_label in enumerate(nb_classifier.classes_):
        print(f"  Class '{c_label}':")

        # Loop through each category value and its corresponding log-probability
        for cat_val, log_p in zip(categories, log_probs[c_idx]):
            # Use np.exp() to convert log-probability back into standard decimal (0 to 1)
            cat_prob = np.exp(log_p)
            print(f"    -> Category '{cat_val}': P = {cat_prob:.3f}")

print(f"=" * 40)

# ==========================================
# TESTING AND RESULTS
# ==========================================

# Test model
y_pred = nb_classifier.predict(X_test)

# Generate and plot confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot the visual confusion matrix
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Bad', 'Good'])
disp.plot(ax=ax, cmap='Blues', values_format='d')

plt.title("Testing Set Confusion Matrix", fontsize=14, pad=15)

# Export the matrix to a file for better viewing:
    # Save as a high-resolution PNG
plt.savefig("naive_bayes_confusion_matrix.png", dpi=300, bbox_inches='tight')

# Calculate model score by combining confusion and cost matrix (from 'Metadata' sheet) together.
    # The cost matrix is defined as follows: [[True Good, False Good], [False Bad, True Bad]] = 
cost_matrix = np.array([[0, 5], 
                        [1, 0]])

# Compute the total error cost by multiplying the confusion matrix with the cost matrix and summing the result
total_model_cost = np.multiply(cm, cost_matrix).sum()
print(f"Total Cost of Model Errors on Testing Set: {total_model_cost}")

