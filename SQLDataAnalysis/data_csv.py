import pandas as pd

df = pd.read_csv('/home/moses/weather_data.csv')

# Check column names
print(df.columns)

df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%m/%d/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M:%S')

if 'Data/Time' in df.columns:
    df.drop(columns=['Data/Time'], inplace=True)

df.rename(columns={
    'Date/Time': 'Date_Time',
    'Dew Point Temp_C': 'Dew_Point_Temp_C',
    'Rel Hum_%': 'Rel_Hum_Percent',
    'Wind Speed_km/h': 'Wind_Speed_kmh',
    'Weather': 'Weather_Condition'
}, inplace=True)

print(df.head(10))

df.to_csv('/home/moses/weather_data_processed.csv', index=False)


