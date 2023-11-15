import pandas as pd
import numpy as np

data = {
    "Name": ['Peter', 'Moses', 'Joyce', 'George', 'Phylis', 'Faith', 'Eliud'],
    "Age": [25, 30, 22, 28, 34, 25, 19],
    "Gender": ['Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    "Marks": [85, 92, np.nan, 88, np.nan, 78, 89]
}

my_data = pd.DataFrame(data)
print("----------Our original Dataset----------")
print(my_data)
print("---------------------------\n")
my_data['Marks'] = pd.to_numeric(my_data['Marks'], errors='coerce')
my_data = my_data[my_data['Marks'] >= 80]
my_data = my_data.drop(['Age'], axis=1)
print("--------------Filtered Dataset------------\n")
print(my_data)