# Wrangling data using Group by

import pandas as pd

studentDetails = {
    'IDNO': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Peter', 'Joyce', 'Geaorge', 'Phylis', 'Moses', 'Pricilla', 'Eliud', 'Veronica', 'John', 'Juliet'],
    'Campus': ['Main', 'Ruiru', 'Nairobi', 'Main', 'Ruiru', 'Ruiru', 'Nairobi', 'Main', 'Main', 'Nairobi']
}

data_1 = pd.DataFrame(studentDetails)
print("\n___________Our first student data to be merged_________\n")
print(data_1)
print("\n-----------------------\n")
feeDetails = {
    'IDNO': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'PENDING': [6000, 375, 0, 7640, 3800, 0, 900, 5200, 0, 1250]
}
data_2 = pd.DataFrame(feeDetails)
print("\n_______________Our second student data to be merged____________\n")
print(data_2)

#Merging dataframes
mergedData = pd.merge(left=data_1, right=data_2, on='IDNO')
print("\n__________Our merged dataframe__________")
print(mergedData)

# Grouping the merged dataframes by campus and calculating the  #  ......total pending fee for each campus
campus_total_fees = mergedData.groupby('Campus')['PENDING'].sum().reset_index()

new_data = campus_total_fees.sort_values(by='PENDING', ascending=True)

print("\n------------Total pending fees for each campus------------\n")
print(campus_total_fees)
