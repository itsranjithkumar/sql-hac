1.# Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

# sol

# select distinct city from station where city REGEXP '^[^aeiou]';


# 2.Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

# sol
#    Select distinct city from station where city not rlike '^[AEIOU].*[AEIOU]$'.

# 3.Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

# sol

# SELECT NAME FROM STUDENTS WHERE MARKS>75 ORDER BY RIGHT (NAME, 3) , ID;

# 4.Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

# sol

# select name from employee order by name ASC;

