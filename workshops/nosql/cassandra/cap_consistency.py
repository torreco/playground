from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

from cassandra import ConsistencyLevel

cass_cluster = Cluster(['cassandra-2'])
cass_session = cass_cluster.connect()
cass_session.set_keyspace('torre')

# CP
# If we choose consistency and partition tolerance: Take down a node and force ConsistencyLevel.ALL
# We can see the database returns an error because it can't guarantee consistency and this we loose availability
stm = SimpleStatement("SELECT * FROM student_grades WHERE student_id = %s", consistency_level=ConsistencyLevel.ALL)
res = cass_session.execute(stm, (1,))
for row in res:
    print(row)