# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
# load the dataset and drop the Loan_ID
banks= bank.drop(columns='Loan_ID')


# check  all the missing values filled.

print(banks.isnull().sum())

# apply mode 

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].shape[0]

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].shape[0]

percentage_se = loan_approved_se * 100 / 614

percentage_nse = loan_approved_nse * 100 / 614

print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here




loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)

big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)
# code ends here


# --------------
# code starts here




loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()

print(mean_values)
# code ends here


