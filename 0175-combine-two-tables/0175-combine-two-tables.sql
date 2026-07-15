# Write your MySQL query statement below
SELECT a.firstName ,a.lastName, b.city , b.state FROM Person a left join Address b on a.personId=b.personId;
