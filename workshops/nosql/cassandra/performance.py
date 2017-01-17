import time

import MySQLdb
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

from cassandra import ConsistencyLevel

mysql_conn = MySQLdb.connect(host="nosql-mysql", user="root", db="torre")

cass_cluster = Cluster(['cassandra-2'])
cass_session = cass_cluster.connect()
cass_session.set_keyspace('torre')

mysql_cursor = mysql_conn.cursor()

start_time = time.time()
for student_id in range(1, 1000):
    mysql_cursor.execute(
        """
        select s.student_id, c.course_id, c.name, p.name, sum(g.value * g.weight)
        from student s
        inner join enroll e on e.student_student_id = s.student_id
        inner join course c on c.course_id = e.course_course_id
        inner join professor p on p.professor_id = c.professor_professor_id
        inner join grade g on g.enroll_enroll_id = e.enroll_id
        where s.student_id = %s
        group by 1, 2, 3, 4
        """,
        (student_id,)
    )
    res = mysql_cursor.fetchall()
end_time = time.time()
print("Time querying students via MySQL: {diff}".format(diff=(end_time - start_time) * 1000))

start_time = time.time()
cass_stm = SimpleStatement("select * from student_grades where student_id = %s", consistency_level=ConsistencyLevel.ONE)
for student_id in range(1, 1000):
    res = cass_session.execute(cass_stm, (student_id,))
end_time = time.time()
print("Time querying students via Cassandra: {diff}".format(diff=(end_time - start_time) * 1000))

print("END")
