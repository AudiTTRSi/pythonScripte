CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);


INSERT INTO Persons (LastName,FirstName,Age)
VALUES ('Kepa','Sandi','59'),
       ('Kepa','Irena','52');



/*
hire_date column is date format, with following  querry counting all the events per year

*/
select
  year(hire_date)as Year, Count(1) as hire_count
from
  employees
GROUP BY year(hire_date)
ORDER BY 1;
