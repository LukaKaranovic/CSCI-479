import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
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

# Function to group 'purpose' categories into broader sets that have similar semantic meaning.
def group_purpose(purpose_value):
    val = str(purpose_value).strip().lower()
    if any(car in val for car in ['new car', 'used car', 'repairs']):
        return 'vehicle'
    elif any(home in val for home in ['furniture/equipment', 'radio/tv', 'domestic appliance']):
        return 'home_appliances'
    elif any(edu in val for edu in ['education', 'retraining', 'business']):
        return 'education_business'
    else:
        return 'other'

# Apply the grouping to both training and testing raw data before encoding
train_df['purpose'] = train_df['purpose'].apply(group_purpose)
test_df['purpose'] = test_df['purpose'].apply(group_purpose)

# Perform data analysis on the new purpose categorizations:
    # Get each value and its frequency count
col = train_df['purpose']._append(test_df['purpose'])
cardinality = col.nunique()
print(f"Number of categories: {cardinality}")
print(f"{'Value':<35} | Frequency")
print("-" * 50) 
counts = col.value_counts()
for val, freq in counts.items():
    print(f"{val:<35} | {freq}")
print("=" * 80) 

# Print the string names found in the first row (headers) to confirm all columns were loaded correctly
print("Loaded columns:", train_df.columns.tolist())

features = ['purpose', 'employment', 'housing', 'job', 'foreign_worker']
target = 'Credit_Risk' 


# Separate descriptive features (X) and target (y) for both sets
X_train_raw = train_df[features]
y_train = train_df[target]

X_test_raw = test_df[features]
y_test = test_df[target]

# === NOTE ===
# Scikit-learn's standard decision tree algorithm cannot process raw text strings and will throw a ValueError if you try to pass text directly.
# Therefore we must convert categorical attributes to numerical. We will be using One-Hot Encoding (map each category to a new boolean attribute containing 0 or 1 as its value).


# Combine train and test datasets before One-Hot Encoding 
# This guarantees both sets have the exact same encoded feature columns
combined_X = pd.concat([X_train_raw, X_test_raw], axis=0)
encoded_X = pd.get_dummies(combined_X, drop_first=True)

# Split back into training and testing sets based on original lengths
X_train = encoded_X.iloc[:len(train_df)]
X_test = encoded_X.iloc[len(train_df):]

# ================================
# BUILDING THE DECISION TREE MODEL
# ================================

# Initialize and train the Decision Tree
clf = DecisionTreeClassifier(
    criterion='gini',   # The function to measure the quality of a split.
    max_depth=4,        # Maximum height of the tree
    random_state=42   
)
clf.fit(X_train, y_train)

# This turns labels for One-Hot Encoded columns like "employment_unemployed" into readable labels like "(employment == unemployed)"
readable_feature_names = []
for col in X_train.columns:
    if '_' in col:
        # Split at the first underscore separating the feature name and its category value
        feat_name, category_val = col.split('_', 1)
        readable_feature_names.append(f"({feat_name} == {category_val})")
    else:
        readable_feature_names.append(col)


# Display the tree rules / structure as plain text in the console 
tree_rules = export_text(clf, feature_names=readable_feature_names)
print("Decision Tree Rules:\n", tree_rules)

# Plot the visual decision tree
fig, ax = plt.subplots(figsize=(32, 14), dpi=300)

plot_tree(
    clf, 
    ax=ax,
    feature_names=readable_feature_names, 
    class_names=['Bad', 'Good'], 
    filled=True, 
    rounded=True,
    fontsize=10,
    precision=2,
    impurity=True
)

ax.axis('off')

plt.title("Decision Tree for German Credit Risk", fontsize=34, pad=15)

# Export the tree to a file for better viewing:
    # Save as a high-resolution PNG
plt.savefig("decision_tree_output.png", dpi=300, bbox_inches='tight')

# ================================
# TESTING
# ================================


# Test the model and generate the Confusion Matrix
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Plot the visual confusion matrix
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Bad', 'Good'])
disp.plot(ax=ax, cmap='Blues', values_format='d')

plt.title("Testing Set Confusion Matrix", fontsize=14, pad=15)

# Export the matrix to a file for better viewing:
    # Save as a high-resolution PNG
plt.savefig("decision_tree_confusion_matrix.png", dpi=300, bbox_inches='tight')

# Calculate model score by combining confusion and cost matrix (from 'Metadata' sheet) together.
    # The cost matrix is defined as follows: [[True Good, False Good], [False Bad, True Bad]] = 
cost_matrix = np.array([[0, 5], 
                        [1, 0]])

# Compute the total error cost by multiplying the confusion matrix with the cost matrix and summing the result
total_model_cost = np.multiply(cm, cost_matrix).sum()
print(f"Total Cost of Model Errors on Testing Set: {total_model_cost}")
