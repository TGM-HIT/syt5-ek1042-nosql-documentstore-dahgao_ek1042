from copy import Error
from datetime import timedelta
import os
from fastapi import FastAPI
import dotenv

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster

# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import ClusterOptions, ClusterTimeoutOptions, QueryOptions

dotenv.load_dotenv()

# Update this to your cluster
ip = os.environ["IP"]
username = os.environ['COUCH_USER']
password = os.environ['COUCH_PASSWORD']
bucket_name = "uwu-bucket"
# User Input ends here.

app = FastAPI()

# Connect options - authentication
auth = PasswordAuthenticator(
    username,
    password,
)

# Get a reference to our cluster
# NOTE: For TLS/SSL connection use 'couchbases://<your-ip-address>' instead
cluster = Cluster(f"couchbase://{ip}", ClusterOptions(auth))

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))

print("cluster ready")

# get a reference to our bucket
bucket = cluster.bucket(bucket_name)
coll = bucket.default_scope().collection("beer-sample")

@app.post('/{key}')
def createData(key: str, body: dict):
    res = coll.upsert(key, body)
    return res

@app.get('/{key}')
def readData(key: str):
    try:
        res = coll.get(key)
        return res.content_as[dict]
    except Exception as e:
        print(e)
        return False

@app.put('/{key}')
def updateData(key: str, body: dict):
    coll.upsert(key, body)

@app.delete('/{key}')
def deleteData(key: str):
    try:
        coll.remove(key)
    except Exception as e:
        print(e)
        return False



# try:
#     # key will equal: "airline_8091"
#     key = 'uwu'
#     result = coll.upsert(key, {'owo': 3})
#     print(result.cas)
#     result = coll.get(key)
#     print(result.content_as[dict])
# except Exception as e:
#     print(e)
#
# cb_coll = cb.scope("inventory").collection("airline")


# Get a reference to the default collection, required for older Couchbase server versions
# cb_coll_default = cb.default_collection()

# upsert document function

#
# def upsert_document(doc):
#     print("\nUpsert CAS: ")
#     try:
#         # key will equal: "airline_8091"
#         key = doc["type"] + "_" + str(doc["id"])
#         result = cb_coll.upsert(key, doc)
#         print(result.cas)
#     except Exception as e:
#         print(e)
#
# # get document function
#
#
# def get_airline_by_key(key):
#     print("\nGet Result: ")
#     try:
#         result = cb_coll.get(key)
#         print(result.content_as[str])
#     except Exception as e:
#         print(e)
#
# # query for new document by callsign
#
#
# def lookup_by_callsign(cs):
#     print("\nLookup Result: ")
#     try:
#         inventory_scope = cb.scope('inventory')
#         sql_query = 'SELECT VALUE name FROM airline WHERE callsign = $1'
#         row_iter = inventory_scope.query(
#             sql_query,
#             QueryOptions(positional_parameters=[cs]))
#         for row in row_iter:
#             print(row)
#     except Exception as e:
#         print(e)
#
#
# airline = {
#     "type": "airline",
#     "id": 8091,
#     "callsign": "CBS",
#     "iata": None,
#     "icao": None,
#     "name": "Couchbase Airways",
# }
#
# upsert_document(airline)
#
# get_airline_by_key("airline_8091")
#
# lookup_by_callsign("CBS")
