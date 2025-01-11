--Ex 1
CREATE TABLE "courses" (
	"course_id"	INTEGER,
	"topic"	TEXT,
	"hours"	INTEGER,
	PRIMARY KEY("course_id" AUTOINCREMENT)
);
CREATE TABLE "students" (
	"student_id"	INTEGER,
	"name"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("student_id" AUTOINCREMENT)
);
CREATE TABLE "grades" (
	"student_id"	INTEGER,
	"course_id"	INTEGER,
	"grade"	INTEGER,
	PRIMARY KEY(student_id,course_id)
	FOREIGN KEY(student_id) REFERENCES students(student_id)
	FOREIGN KEY(course_id) REFERENCES courses(course_id)
);

--Ex 2
INSERT INTO courses (topic, hours) VALUES ('Maths', 120);
INSERT INTO courses (topic, hours) VALUES ('Science', 132);
INSERT INTO courses (topic, hours) VALUES ('Literature', 98);
INSERT INTO courses (topic, hours) VALUES ('Finance', 107);

INSERT INTO students (name, email) VALUES ('John Doe', 'johndoe1@gmail.com');
INSERT INTO students (name, email) VALUES ('Jane Doe', 'janedoe2@gmail.com');

INSERT INTO grades (student_id, course_id,grade) VALUES (1, 1,98);
INSERT INTO grades (student_id, course_id,grade) VALUES (1, 2,87);
INSERT INTO grades (student_id, course_id,grade) VALUES (1, 3,91);
INSERT INTO grades (student_id, course_id,grade) VALUES (1, 4,95);
INSERT INTO grades (student_id, course_id,grade) VALUES (2, 1,99);
INSERT INTO grades (student_id, course_id,grade) VALUES (2, 2,86);
INSERT INTO grades (student_id, course_id,grade) VALUES (2, 3,79);
INSERT INTO grades (student_id, course_id,grade) VALUES (2, 4,89);

--Ex 3
SELECT topic, avg(grades.grade)
FROM grades
JOIN courses ON courses.course_id=grades.course_id
GROUP BY grades.course_id