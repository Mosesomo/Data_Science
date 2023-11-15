# Dealing with the missing values in the data
import pandas as pd
import numpy as np

data = {
    "Name": ['Peter', 'Moses', 'Joyce', 'George', 'Phylis', 'Faith', 'Eliud'],
    "Age": [25, 30, 22, 28, 34, 25, 19],
    "Gender": ['Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
    "Marks": [85, 92, 'NaN', 88, 'NaN', 78, 89]
}

my_data = pd.DataFrame(data)
print(my_data)
print()
sum = count = 0
for i in my_data['Marks']:
    if str(i).isnumeric():
        count += 1
        sum += int(i)
mean = sum / count
print("Mean: {}".format(mean))
my_data = my_data.replace(to_replace="NaN", value=mean)
print("+++++++New Data+++++++++++++++\n")
print(my_data)
print()
# filtering elements in the dataset

my_data = my_data[my_data['Marks'] >= 80]
my_data = my_data.drop(['Age'], axis=1)
print("---------Filtered Data-----------\n")
print(my_data)