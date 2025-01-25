-- a
SELECT c.course_id, c.course_name, l.first_name, l.last_name FROM courses c
INNER JOIN lecturers l
on c.lecturer_id = l.lecturer_id

-- b
SELECT c.course_id, c.course_name FROM courses c
LEFT JOIN lecturers l
on c.lecturer_id = l.lecturer_id
WHERE c.lecturer_id is NULL

-- c
SELECT c.course_id, c.course_name, l.first_name, l.last_name FROM courses c
LEFT JOIN lecturers l
on c.lecturer_id = l.lecturer_id

-- d
SELECT l.lecturer_id, l.first_name, l.last_name, c.course_name FROM lecturers l
INNER JOIN courses c
on l.lecturer_id = c.lecturer_id

-- e
SELECT l.lecturer_id, l.first_name, l.last_name FROM lecturers l
LEFT JOIN courses c
on l.lecturer_id = c.lecturer_id
WHERE c.lecturer_id is NULL

-- f
SELECT l.lecturer_id, l.first_name, l.last_name, c.course_name FROM lecturers l
LEFT JOIN courses c
on l.lecturer_id = c.lecturer_id

-- g
SELECT  c.course_id, c.course_name, l.lecturer_id, l.first_name, l.last_name FROM courses c
FULL OUTER JOIN lecturers l
on c.lecturer_id = l.lecturer_id

-- h
SELECT l.first_name, l.last_name, c.course_name  FROM courses c
CROSS JOIN lecturers l
ORDER by l.first_name