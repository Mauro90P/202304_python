USE world;

/* Ejercio de prgunta N°1*/ #OK
SELECT name,country_code,language,percentage
FROM languages
INNER JOIN countries
ON languages.country_code = countries.code
WHERE language = "Slovene"
ORDER BY percentage DESC;

/* Ejercio de prgunta N°2*/ #OK

SELECT name,language,country_id
FROM languages
INNER JOIN cities
ON languages.country_id = cities.country_id
ORDER BY country_id DESC;
SELECT * FROM cities
/* Ejercio de prgunta N°3*/ ##OK
SELECT name, country_code,population,country_id
FROM cities
WHERE country_id = 136
ORDER BY population >500000 DESC;

/* Ejercio de prgunta N°4*/ ###okkkkkkkk

SELECT name,language,percentage 
FROM languages
INNER JOIN countries
ON countries.id = languages.country_id
ORDER BY percentage DESC;

/* Ejercio de prgunta N°5*/ ###OKKKK
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;
/* Ejercio de prgunta N°6*/
SELECT name, government_form,capital,life_expectancy 
FROM countries
WHERE capital > 200 AND life_expectancy > 75;

/* Ejercio de prgunta N°7*/ ##OKKK

SELECT countries.name,cities.name,cities.district,cities.population
FROM  countries
INNER JOIN cities
ON cities.country_id = countries.id
WHERE district = 'Buenos Aires';
/* Ejercio de prgunta N°8*/

SELECT region, COUNT(id)
FROM countries
group by region
ORDER BY COUNT(id) DESC;



