import pandas as pd

# Loading the CSV file into a DataFrame
df = pd.read_csv('/home/moses/Data_Science/web_scraping/graduands_list.csv')

# Filter the DataFrame for rows where the 'Year' column is 2024
graduands_2024 = df[df['Year'] == 2024]

# Count the number of graduands in 2024
count_graduands_2024 = graduands_2024.shape[0]
print(f'Total graduands in 2024: {count_graduands_2024}')


print(graduands_2024.head(15))

# Saving the filtered DataFrame to a new CSV file
graduands_2024.to_csv('/home/moses/Data_Science/web_scraping/graduands_list_2024.csv', index=False)
