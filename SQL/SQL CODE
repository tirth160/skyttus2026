 create database student;
 create table  student(
  student_id INT,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT
)
insert into student values
(1,'tirth','cse','4','90'),
(2,'fenil','che','4','80'),
(3,'max','che','3','70'),
(4,'jeet','cse','4','60'),
(5,'rex','cse','4','50');

Tasks

--Display all student records
SELECT * FROM student;


--Display only name and department
SELECT name, department 
FROM student;


--Find students with marks greater than 75
SELECT * FROM student 
WHERE marks > 75;


--Display students from CSE department
SELECT * 
FROM student 
WHERE department = 'CSE';

--Display top 3 scorers
SELECT TOP 3 * 
FROM student 
ORDER BY marks DESC;
