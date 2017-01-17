import random

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", db="torre")

cursor = db.cursor()
cursor.execute("select course_id, name from course")
courses = cursor.fetchall()
for (course_id, course_name) in courses:
    # Enroll 30 random students
    cursor.execute("select student_id from student order by RAND() limit 30")
    students = cursor.fetchall()
    for (student_id,) in students:
        cursor.execute("insert into enroll(student_student_id, course_course_id) values(%s, %s)",
                       (student_id, course_id))
        db.commit()

        cursor.execute("select enroll_id from enroll where student_student_id = %s and course_course_id = %s",
                       (student_id, course_id))
        enroll_id = cursor.fetchone()
        # Insert 3 grades for each student enrolled
        for grade_suffix in ["for dummies", "for experts", "and beyond"]:
            cursor.execute("insert into grade(enroll_enroll_id, value, weight, name) values (%s, %s, %s, %s)",
                           (enroll_id, random.randrange(1, 50, 1) / 10, 0.33, "%s %s" % (course_name, grade_suffix)))
            db.commit()

print("End")
