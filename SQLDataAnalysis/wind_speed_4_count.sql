-- number of times the wind speed was exactly 4 km/hr

SELECT COUNT(*) AS windSpeed4Count
FROM weather_data
WHERE Wind_Speed_kmh = 4;

