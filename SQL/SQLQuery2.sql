--Count total number of students

SELECT COUNT(*) AS total_students
FROM students;

--total number of students
SELECT AVG(marks) AS average_marks
FROM students;

--find highest and lowest marks
SELECT 
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM students;

--Find department-wise average marks
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

--Display departments where average marks > 7
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
