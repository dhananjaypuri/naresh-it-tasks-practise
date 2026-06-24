# Loan Data Preprocessing & Feature Engineering Project

## Overview

This project demonstrates a comprehensive data preprocessing and feature engineering pipeline for loan approval prediction. The workflow transforms raw loan data through multiple stages of cleaning, exploration, outlier treatment, and feature transformation, resulting in a clean, model-ready dataset.

## Dataset

**File:** `LoanData.csv`

### Original Features
- **Applicant Information:** Gender, Married, Dependents, Education, Self_Employed
- **Financial Information:** ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term
- **Loan Details:** Loan_ID, Credit_History, Property_Area
- **Target Variable:** Loan_Status (binary classification: Y/N)

## Data Pipeline Flow

```mermaid
graph TD
    A["📊 Raw Data: LoanData.csv"] --> B["🔍 Data Exploration<br/>Q1-Q3"]
    B --> C["📋 Data Quality Check<br/>Q4-Q7"]
    C --> D["🧹 Data Cleaning<br/>Q8-Q10"]
    D --> E["📌 Feature Categorization<br/>Q11-Q12"]
    E --> F["🎯 Outlier Detection & Treatment<br/>Q14-Q16"]
    F --> G["✨ Feature Engineering<br/>Q18-Q23"]
    G --> H["🔐 Encoding Categories<br/>Q25-Q30"]
    H --> I["✅ Data Finalization<br/>Q31-Q35"]
    I --> J["💾 Cleaned Data:<br/>Cleaned_tranformed_loandata.csv"]
    
    style A fill:#e1f5ff
    style J fill:#c8e6c9
    style D fill:#fff9c4
    style F fill:#ffccbc
    style G fill:#f0f4c3
    style H fill:#dcedc8
```

## Project Pipeline

### 1. **Data Loading & Exploration** (Q1-Q3)
- Load the dataset into a Pandas DataFrame
- Display dataset shape, columns, data types
- Print head and tail samples
- Generate descriptive statistics

### 2. **Data Quality Assessment** (Q4-Q7)
- Identify missing values and calculate missing value percentages
- Detect duplicate records
- Check for duplicate Loan_IDs

### 3. **Data Cleaning** (Q8-Q10)

```mermaid
graph TD
    A["Raw Data with Issues"] --> B{"Missing<br/>Values?"}
    B -->|Numerical Col| C["Fill with Median"]
    B -->|Categorical Col| D["Fill with Mode"]
    C --> E["✅ Missing Values Handled"]
    D --> E
    E --> F{"Duplicate<br/>Records?"}
    F -->|Yes| G["Remove Duplicates"]
    F -->|No| H["No Action"]
    G --> I["✅ Verification:<br/>No Missing Values<br/>No Duplicates"]
    H --> I
    
    style A fill:#ffccbc
    style E fill:#fff9c4
    style I fill:#c8e6c9
```

### 4. **Feature Categorization** (Q11-Q12)
- Separate features into numerical and categorical columns
- Display unique values for categorical features
- Identify features with ≤10 unique values

### 5. **Outlier Detection & Treatment** (Q14-Q16)

```mermaid
graph LR
    A["Data Distribution"] --> B["Calculate Q1<br/>Q3, IQR"]
    B --> C["Q1 - 1.5×IQR<br/>Lower Limit"]
    B --> D["Q3 + 1.5×IQR<br/>Upper Limit"]
    C --> E["🎯 Outlier Range"]
    D --> E
    E --> F["Values < LL"]
    E --> G["Values > UL"]
    E --> H["Normal Values<br/>LL ≤ x ≤ UL"]
    
    F -->|Replace with LL| I["✅ Treated<br/>Data"]
    G -->|Replace with UL| I
    H -->|Keep as is| I
    
    style E fill:#ffccbc
    style I fill:#c8e6c9
    
    J["Applied to:<br/>ApplicantIncome<br/>CoapplicantIncome<br/>LoanAmount"]
    J -.-> I
```

**Methodology:**
- Calculate Q1, Q3, and IQR
- Lower Limit = Q1 - 1.5 × IQR
- Upper Limit = Q3 + 1.5 × IQR
- Cap outliers at lower and upper bounds

### 6. **Feature Engineering** (Q18-Q23)

```mermaid
graph LR
    A["ApplicantIncome<br/>CoapplicantIncome"] -->|Addition| B["TotalIncome"]
    B -->|Divide by Dependents| C["IncomePerDependent"]
    B -->|Feature 1| E["🎯 ML Features"]
    D["LoanAmount"] -->|Divide by TotalIncome| F["LoanIncomeRatio"]
    F -->|Feature 2| E
    B -->|Categorize<br/>Low/Medium/High| G["Inc_Category"]
    G -->|Feature 3| E
    H["Loan_Amount_Term"] -->|Divide by 12| I["Loan_Term_Years"]
    I -->|Feature 4| E
    
    style B fill:#bbdefb
    style E fill:#c8e6c9
    style F fill:#bbdefb
    style G fill:#bbdefb
    style I fill:#bbdefb
```

#### Created Features:
| Feature | Formula | Purpose |
|---------|---------|---------|
| **TotalIncome** | ApplicantIncome + CoapplicantIncome | Total household income |
| **IncomePerDependent** | TotalIncome / Dependents | Income normalized by dependents |
| **LoanIncomeRatio** | LoanAmount / TotalIncome | Debt-to-income proxy |
| **Inc_Category** | Low/Medium/High based on mean | Income segmentation |
| **Loan_Term_Years** | Loan_Amount_Term / 12 | Loan duration in years |

### 7. **Encoding Categorical Variables** (Q25-Q30)

```mermaid
graph TD
    A["Categorical Features"] --> B["Binary Features"]
    A --> C["Ordinal Features"]
    A --> D["Nominal Features"]
    
    B -->|Gender| E["Label Encoding<br/>Male→1, Female→0"]
    B -->|Married| F["Manual Mapping<br/>Yes→1, No→0"]
    B -->|Self_Employed| G["Label Encoding<br/>Yes→1, No→0"]
    
    C -->|Education| H["Ordinal Encoding<br/>Not Graduate→0<br/>Graduate→1"]
    C -->|Inc_Category| I["Ordinal Encoding<br/>Low→0, Medium→1<br/>High→2"]
    C -->|Loan_Status| J["Label Encoding<br/>N→0, Y→1<br/>TARGET ✓"]
    
    D -->|Property_Area| K["One-Hot Encoding<br/>Urban→1,0,0<br/>Rural→0,1,0<br/>Semiurban→0,0,1"]
    
    E --> L["✅ All Features<br/>Numeric Ready"]
    F --> L
    G --> L
    H --> L
    I --> L
    J --> L
    K --> L
    
    style J fill:#ffcdd2
    style L fill:#c8e6c9
```

| Column | Encoding Method | Details |
|--------|-----------------|---------|
| Gender | Label Encoding | Binary encoding |
| Married | Manual Mapping | Yes→1, No→0 |
| Self_Employed | Label Encoding | Binary encoding |
| Education | Ordinal Encoding | Not Graduate→0, Graduate→1 |
| Loan_Status | Label Encoding | Target variable (N→0, Y→1) |
| Property_Area | One-Hot Encoding | Creates 3 binary columns |
| Inc_Category | Ordinal Encoding | Low→0, Medium→1, High→2 |

### 8. **Data Finalization** (Q31-Q35)
- Drop non-numeric columns verification
- Remove redundant columns (Loan_ID, ApplicantIncome, CoapplicantIncome, IncomePerDependent, Inc_Category)
- Generate correlation analysis with target variable
- Export cleaned dataset to `Cleaned_tranformed_loandata.csv`

## Output Dataset

**File:** `Cleaned_tranformed_loandata.csv`

Final dataset with:
- All categorical variables encoded
- Feature engineering applied
- Outliers treated
- Missing values handled
- Ready for machine learning models

## Key Insights

### Data Quality Issues Found & Resolution

```mermaid
graph LR
    A["📊 Raw Data<br/>Quality Issues"] --> B["Missing Values<br/>in Multiple Columns"]
    A --> C["Duplicate<br/>Records"]
    A --> D["Outliers in<br/>Income & Loan Amount"]
    
    B -->|Median/Mode<br/>Imputation| E["✅ Cleaned<br/>Dataset"]
    C -->|Drop Duplicates| E
    D -->|IQR Method| E
    
    F["Correlations with<br/>Loan_Status"] -->|Feature Selection| E
    
    E --> G["🚀 Ready for<br/>ML Models"]
    
    style A fill:#ffccbc
    style E fill:#c8e6c9
    style G fill:#a5d6a7
```

- Missing values in multiple columns (imputed with median/mode)
- Duplicate records (removed)
- Outliers in income and loan amount (treated using IQR method)

### Feature Correlations
The project computes correlation coefficients with Loan_Status to identify influential features for predictive modeling.

## Technologies Used

```mermaid
graph LR
    A["Python 3.x"] --> B["Data Science Stack"]
    B --> C["Pandas"]
    B --> D["NumPy"]
    B --> E["Scikit-learn"]
    
    C -->|Data Manipulation| F["Transform &<br/>Analyze"]
    D -->|Numerical Ops| F
    E -->|ML Preprocessing| G["LabelEncoder<br/>OrdinalEncoder<br/>OneHotEncoder"]
    
    F --> H["✅ Model-Ready<br/>Dataset"]
    G --> H
    
    style B fill:#e3f2fd
    style H fill:#c8e6c9
```

## Technologies Used

- **Python 3.x**
- **Pandas:** Data manipulation and analysis
- **NumPy:** Numerical computations
- **Scikit-learn:** Preprocessing (LabelEncoder, OrdinalEncoder, OneHotEncoder)

## Project Structure

```
ML/
├── loan_project.ipynb                    # Main notebook with full pipeline
├── LoanData.csv                          # Original raw dataset
├── Cleaned_tranformed_loandata.csv       # Processed output dataset
├── linear_reg_model.ipynb                # Linear regression model
├── train_split_cv.ipynb                  # Train-test split and cross-validation
└── README.md                             # This file
```

## Usage

1. **Load the notebook:**
   ```bash
   jupyter notebook loan_project.ipynb
   ```

2. **Run all cells sequentially** to execute the complete pipeline

3. **Output:** Access the cleaned dataset at `Cleaned_tranformed_loandata.csv`

## Questions Addressed (Q1-Q31)

The notebook systematically answers 31 data science questions including:
- Data exploration and profiling
- Missing value and duplicate handling
- Outlier detection and treatment
- Feature engineering and transformation
- Encoding strategies
- Data validation and quality checks

## Next Steps

### Model Development Workflow

```mermaid
graph LR
    A["Cleaned Dataset"] --> B["Train-Test Split"]
    B --> C["Classification Models"]
    C --> D["Logistic Regression"]
    C --> E["Decision Trees"]
    C --> F["Ensemble Methods"]
    D --> G["🎯 Model Evaluation"]
    E --> G
    F --> G
    G --> H["Cross-Validation"]
    H --> I["Loan Approval<br/>Predictions ✓"]
    
    style A fill:#c8e6c9
    style I fill:#a5d6a7
```

This cleaned dataset can be used for:
- Classification models (Loan approval prediction)
- Feature importance analysis
- Interpretability studies
- Ensemble methods
- Cross-validation and hyperparameter tuning

## Notes

- All transformations are reversible through proper documentation
- Encoding choices follow standard practices for loan prediction models
- The pipeline is modular and can be adapted for similar datasets
