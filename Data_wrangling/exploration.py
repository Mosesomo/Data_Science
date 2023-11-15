import pandas as pd

data = {
    "Name": ['Peter', 'Moses', 'Joyce', 'George', 'Phylis', 'Faith', 'Eliud'],
    "Age": [25, 30, 22, 28, 34, 25, 19],
    "Gender": ['Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    "Marks": [85, 92, 'NaN', 88, 'NaN', 78, 89]
}

my_data = pd.DataFrame(data)
print(my_data)