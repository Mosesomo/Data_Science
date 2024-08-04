-- Number of records where wind speed > 24 km/hr and visibility = 25 km

SELECT COUNT(*) AS windSpeedVisibility
FROM weather_data
WHERE Wind_Speed_kmh > 24 AND Visibility_km = 25;


-- Mean value of each column for each weather condition

SELECT
Weather_Condition,
    AVG(Temp_C) AS Avg_Temp_C,
    AVG(Dew_Point_Temp_C) AS Avg_Dew_Point_Temp_C,
    AVG(Rel_Hum_Percent) AS Avg_Rel_Hum_Percent,
    AVG(Wind_Speed_kmh) AS Avg_Wind_Speed_kmh,
    AVG(Visibility_km) AS Avg_Visibility_km,
    AVG(Press_kPa) AS Avg_Press_kPa
FROM weather_data
GROUP BY Weather_Condition;


-- Instances where the weather is clear and the relative humidity > 50, or visibility > 40

SELECT * FROM weather_data
WHERE (Weather_Condition = 'Clear' AND Rel_Hum_Percent > 50) OR Visibility_km > 40;

-- Number of weather conditions that include snow
SELECT COUNT(*) AS SnowConditionsCount
FROM weather_data
WHERE Weather_Condition LIKE '%Snow%';

