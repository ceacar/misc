/*
Let  be the number of CITY entries in STATION, and let  be the number of distinct CITY names in STATION; query the value of  from STATION. In other words, find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

Input Format

The STATION table is described as follows:
ID
CITY
STATE
LAT_N
LONG_W
where LAT_N is the northern latitude and LONG_W is the western longitude.
*/

select count(CITY) - count(DISTINCT CITY) as result from STATION



/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Input Format

The STATION table is described as follows:

Station.jpg

where LAT_N is the northern latitude and LONG_W is the western longitude.

Sample Input

Let's say that CITY only has four entries: DEF, ABC, PQRS and WXY

Sample Output

ABC 3
PQRS 4
Explanation

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with the respective lengths  and . The longest-named city is obviously PQRS, but there are  options for shortest-named city; we choose ABC, because it comes first alphabetically.

Note 
You can write two separate queries to get the desired output. It need not be a single query.
*/
select * 
from(
    select STATION.CITY, CHAR_LENGTH(STATION.CITY) 
    from (select min(CHAR_LENGTH(CITY)) as city_length from STATION ) as s, STATION
    where CHAR_LENGTH(STATION.CITY) = s.city_length
    ORDER BY STATION.CITY ASC
    LIMIT 1) as s
union all
select * 
from(
    select STATION.CITY, CHAR_LENGTH(STATION.CITY) 
    from (select max(CHAR_LENGTH(CITY)) as city_length from STATION ) as s, STATION
    where CHAR_LENGTH(STATION.CITY) = s.city_length
    ORDER BY STATION.CITY DESC
    LIMIT 1) as t


/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/
select CITY
from station
where CITY RLIKE '^[aeiou]'




/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
*/
select distinct CITY
from station
where CITY RLIKE '^.*[aeiou]$'
#below query also work
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','i','e','o','u');

/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
*/
select distinct CITY
from STATION
where 
    RIGHT(LOWER(CITY),1) in ('a', 'e', 'i', 'o','u')
        and
    LEFT(LOWER(CITY),1) in ('a', 'e', 'i', 'o','u')


/*
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
*/


select distinct CITY 
FROM STATION
where CITY not RLIKE '^[aeiou].*[aeiou]$' 

/*
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
^[^AEIOU] mean the field does not start with AEIOU(it is the second "^" indicates it does not start with)
*/

SELECT DISTINCT City
FROM Station
WHERE CITY RLIKE('^[^AEIOU].*[^aeiou]$');

/*
Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
STUDENT:
ID
NAME
MARKS
*/
select name from STUDENTS
where MARKS > 75 
order by RIGHT(NAME,3) asc,ID asc



/*
ou are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table.



If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.

  Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.
Projects:
Task_id
Start_date
End_Date


1, 2015-10-01 2015-10-02
2, 2015-10-02 2015-10-03
3, 2015-11-01 2015-11-02

should output
2015-11-01, 2015-11-02
2015-10-01, 2015-10-03
*/

SET sql_mode = '';
SELECT Start_Date, min(End_Date) # this will do a cross join between two tables
FROM
    (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) a,
    (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) b
WHERE Start_Date < End_Date
GROUP BY Start_Date /*this group by eliminates all the inaccurate records introduced by cross join*/
ORDER BY DATEDIFF(End_Date, Start_Date), Start_Date




/*

You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

Students:
ID
Name

Friends:
ID
Friend_ID

Packages:
ID
Salary


Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.


for example, an intermediate result should be like this:
id name friend_id name salary friend_salary
1 samantha 14 Scarlet 15.5 15.8

*/

select name from ( 
  select s.Name as name, p.Salary as salary, s2.Name as f_name, p2.Salary as f_salary
  from 
    Friends as f left outer join Packages as p on f.ID = p.ID
      left join Packages as p2 on f.Friend_ID = p2.ID
      left join Students as s on s.ID = f.ID
      left join Students as s2 on s2.ID = f.Friend_ID
  having f_salary > salary
  order by f_salary
) as a

/*below solution also work*/
Select S.Name
From ( Students S join Friends F Using(ID)
       join Packages P1 on S.ID=P1.ID
       join Packages P2 on F.Friend_ID=P2.ID)
Where P2.Salary > P1.Salary
Order By P2.Salary;



