-- checking for null values

SELECT
    COUNT(*) AS Total_NULLs
FROM weather_data
WHERE
    Date_Time IS NULL OR
    Temp_C IS NULL OR
    Dew_Point_Temp_C IS NULL OR
    Rel_Hum_Percent IS NULL OR
    Wind_Speed_kmh IS NULL OR
    Visibility_km IS NULL OR
    Press_kPa IS NULL OR
    Weather_Condition IS NULL;

