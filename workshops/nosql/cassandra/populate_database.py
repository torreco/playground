import MySQLdb
from cassandra.cluster import Cluster

mysql_conn = MySQLdb.connect(host="nosql-mysql", user="root", db="torre")

cass_cluster = Cluster(['cassandra-2'])
cass_session = cass_cluster.connect()
cass_session.set_keyspace('torre')

mysql_cursor = mysql_conn.cursor()

print("Students Query")
mysql_cursor.execute(
    """
    select s.student_id, c.course_id, c.name, p.name, sum(g.value * g.weight)
    from student s
    inner join enroll e on e.student_student_id = s.student_id
    inner join course c on c.course_id = e.course_course_id
    inner join professor p on p.professor_id = c.professor_professor_id
    inner join grade g on g.enroll_enroll_id = e.enroll_id
    group by 1, 2, 3, 4
    """
)
for (student_id, course_id, course_name, professor_name, grade) in mysql_cursor.fetchall():
    cass_session.execute(
        """
        INSERT INTO student_grades (student_id, course_id, course_name, professor_name, grade)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (student_id, course_id, course_name, professor_name, grade)
    )

print("Professors Query")
""
mysql_cursor.execute(
    """
    select p.professor_id, s.student_id, s.name, sum(g.value * g.weight)
    from professor p
    inner join course c on c.professor_professor_id = p.professor_id
    inner join enroll e on e.course_course_id = c.course_id
    inner join student s on s.student_id = e.student_student_id
    inner join grade g on g.enroll_enroll_id = e.enroll_id
    group by 1, 2, 3
    """
)
for (professor_id, student_id, student_name, grade) in mysql_cursor.fetchall():
    cass_session.execute(
        """
        INSERT INTO professor_students (professor_id, student_name, grade)
        VALUES (%s, %s, %s)
        """,
        (professor_id, student_name, grade)
    )

print("END")


