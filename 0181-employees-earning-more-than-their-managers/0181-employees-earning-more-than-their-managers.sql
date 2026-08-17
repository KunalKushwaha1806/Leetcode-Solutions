# Write your MySQL query statement below
Select e.name as Employee from employee e join employee m on e.managerId=m.id where e.salary>m.salary; 