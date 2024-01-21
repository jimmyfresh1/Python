SELECT countries.region, COUNT(countries.name) as country_number
FROM countries
GROUP BY countries.region
ORDER BY  country_number DESC