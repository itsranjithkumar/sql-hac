1.# Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

# sol

# select distinct city from station where city REGEXP '^[^aeiou]';


