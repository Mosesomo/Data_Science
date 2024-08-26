import pandas as pd

df = pd.read_csv('/home/moses/Data_Science/web_scraping/graduands_list_2024.csv')

# Filter for different programs
bachelor_degree = df[df['Program'].str.contains('BACHELOR', case=False)]
diploma = df[df['Program'].str.contains('DIPLOMA', case=False)]
certificate = df[df['Program'].str.contains('CERTIFICATE', case=False)]

# Counter number of graduands in each program
print(f'Bachelor Degree Graduands: {bachelor_degree.shape[0]}')
print(f'Diploma Graduands: {diploma.shape[0]}')
print(f'Certicate Graduands: {certificate.shape[0]}')

# Save the categorized programs
bachelor_degree.to_csv('/home/moses/Data_Science/web_scraping/bachelor_degree_graduands.csv', index=False)
diploma.to_csv('/home/moses/Data_Science/web_scraping/diploma_graduands.csv', index=False)
certificate.to_csv('/home/moses/Data_Science/web_scraping/certificate_graduands.csv', index=False)