from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

from cassandra import ConsistencyLevel

cass_cluster = Cluster(['cassandra-2'])
cass_session = cass_cluster.connect()
cass_session.set_keyspace('torre')

# AP
# If we choose availability and partition tolerance, we loose consistency: Take down a node and write a new row,
# it's successful (meaning the database is still available) by the data is no longer consistent among nodes.
stm = SimpleStatement(
    """
        INSERT INTO student_grades (student_id, course_id, course_name, professor_name, grade)
        VALUES (%s, %s, %s, %s, %s)
    """, consistency_level=ConsistencyLevel.ANY)
res = cass_session.execute(stm, (1, 1, 'course', 'professor', 0))
print(res)

# Once the partition is solved, the database might be consistent again or there might be a write conflict
