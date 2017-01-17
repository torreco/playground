import MySQLdb
from neo4j.v1 import GraphDatabase, basic_auth

mysql_conn = MySQLdb.connect(host="nosql-mysql", user="root", db="torre")

neo4j_driver = GraphDatabase.driver("bolt://nosql-neo4j", auth=basic_auth("neo4j", "torre"))
neo4j_session = neo4j_driver.session()

print("Students ...")
mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute("SELECT * FROM student")
for (student_id, name) in mysql_cursor.fetchall():
    neo4j_session.run("CREATE (:Student {student_id: {student_id}, name: {name}})",
                      {'student_id': student_id, 'name': name})

print("Professors ...")
mysql_cursor.execute("SELECT * FROM professor")
for (professor_id, name) in mysql_cursor.fetchall():
    neo4j_session.run("CREATE (:Professor {professor_id: {professor_id}, name: {name}})",
                      {'professor_id': professor_id, 'name': name})

print("Courses ...")
mysql_cursor.execute("SELECT * FROM course")
for (course_id, name, semester, professor_id) in mysql_cursor.fetchall():
    neo4j_session.run("CREATE (:Course {course_id: {course_id}, name: {name}, semester: {semester}})",
                      {'course_id': course_id, 'name': name, 'semester': semester})
    neo4j_session.run(
        """
            MATCH (p: Professor {professor_id: {professor_id}}), (c: Course {course_id: {course_id}})
            CREATE (p)-[:TEACHES]->(c)
        """,
        {'professor_id': professor_id, 'course_id': course_id}
    )

print("Enroll ...")
mysql_cursor.execute(
    """
    select e.student_student_id, e.course_course_id, sum(g.value * g.weight)
    from enroll e
    inner join grade g on g.enroll_enroll_id = e.enroll_id
    group by 1, 2
    """
)
for (student_id, course_id, grade) in mysql_cursor.fetchall():
    neo4j_session.run(
        """
            MATCH (s: Student {student_id: {student_id}}), (c: Course {course_id: {course_id}})
            CREATE (s)-[:TAKES {grade: {grade}}]->(c)
        """,
        {'student_id': student_id, 'course_id': course_id, 'grade': float(grade)}
    )



# mysql_cursor.execute("SELECT * FROM enroll")
# for (enroll_id, student_id, course_id) in mysql_cursor.fetchall():
#     neo4j_session.run(
#         """
#             MATCH (s: Student {student_id: {student_id}}), (c: Course {course_id: {course_id}})
#             CREATE (s)-[:TAKES]->(c)
#         """,
#         {'student_id': student_id, 'course_id': course_id}
#     )

# print("Grades ...")
# mysql_cursor.execute(
#     """
#       SELECT e.student_student_id, e.course_course_id, value, weight, name
#       FROM grade g INNER JOIN enroll e ON e.enroll_id = g.enroll_enroll_id
#     """
# )
# for (student_id, course_id, value, weight, name) in mysql_cursor.fetchall():
#     neo4j_session.run(
#         """
#             MATCH (s: Student {student_id: {student_id}}), (c: Course {course_id: {course_id}})
#             CREATE (s)-[:PARTIAL{value: {value}, weight: {weight}, name: {name}}]->(c)
#         """,
#         {'student_id': student_id, 'course_id': course_id, 'value': float(value), 'weight': float(weight), 'name': name}
#     )

neo4j_session.close()

print("END")
