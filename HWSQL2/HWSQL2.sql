--Ex.1
SELECT course_id, Courses.name, Lecturers.name
FROM Courses
INNER JOIN Lecturers
ON Lecturers.lecturer_id = Courses.lecturer_id

--Ex.2
SELECT course_id, Courses.name, Lecturers.name
FROM Courses
LEFT JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id

--Ex.3
SELECT Lecturers.lecturer_id, Lecturers.name, Courses.name
FROM Courses
RIGHT JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id

--Ex.4
SELECT course_id, Courses.name, Lecturers.name
FROM Courses
LEFT JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id is NULL

--Ex.5
SELECT Lecturers.lecturer_id, Lecturers.name
FROM Courses
RIGHT JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id is NULL

--Ex.6
SELECT Lecturers.name, Courses.name
FROM Courses
FULL OUTER JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id

--Ex.7
SELECT Lecturers.name, Courses.name
FROM Courses
FULL OUTER JOIN Lecturers
ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.lecturer_id is NULL

--Ex.8
SELECT *
FROM Lecturers
WHERE name like "%i%"

--Ex.9
SELECT count(*)
FROM Lecturers

--Ex.10
SELECT count(*)
FROM Courses

--Ex.11
ALTER TABLE Courses
ADD weekly_hours INT

UPDATE Courses
SET weekly_hours = 4
WHERE course_id < 5

UPDATE Courses
SET weekly_hours = 8
WHERE course_id < 9 and course_id > 4

UPDATE Courses
SET weekly_hours = 6
WHERE course_id > 8

--Ex.12
SELECT weekly_hours, count(*)
FROM Courses
GROUP BY weekly_hours

--Ex.13
SELECT Lecturers.name
FROM Lecturers
LEFT JOIN Courses
ON Courses.lecturer_id = Lecturers.lecturer_id
WHERE Courses.weekly_hours = 8

--Ex.14
DELETE FROM Courses
WHERE lecturer_id IS NULL AND weekly_hours = 4

--Ex.15
SELECT Employees.name, Departments.*
FROM Employees
INNER JOIN Departments
ON Employees.department_id = Departments.department_id

--Ex.16
SELECT Employees.name, Departments.name
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id

--Ex.17
SELECT Employees.name, Departments.name
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
WHERE Employees.department_id is NULL

--Ex.18
SELECT Departments.name, count(Employees.employee_id)
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
GROUP BY Departments.department_id

--Ex.19
SELECT Departments.name, avg(Employees.salary)
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
GROUP BY Departments.department_id

--Ex.20
SELECT Departments.name, max(Employees.salary), Employees.name
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
GROUP BY Departments.department_id

--Ex.21
SELECT Employees.name, Employees.seniority, Departments.*
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
ORDER BY Employees.seniority

--Ex.22
SELECT Employees.seniority, avg(Employees.salary)
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id
GROUP BY Employees.seniority

--Ex.23
ALTER TABLE Departments
ADD COLUMN head_count INT

ALTER TABLE Departments
ADD COLUMN average_salary INT

ALTER TABLE Departments
ADD COLUMN max_salary INT

ALTER TABLE Departments
ADD COLUMN average_seniority INT

UPDATE Departments
SET head_count =(
SELECT count(*)
FROM Employees
WHERE Employees.department_id=Departments.department_id
)

UPDATE Departments
SET average_salary =(
SELECT avg(Employees.salary)
FROM Employees
WHERE Employees.department_id=Departments.department_id
)

UPDATE Departments
SET max_salary =(
SELECT max(Employees.salary)
FROM Employees
WHERE Employees.department_id=Departments.department_id
)

UPDATE Departments
SET average_seniority =(
SELECT avg(Employees.seniority)
FROM Employees
WHERE Employees.department_id=Departments.department_id
)