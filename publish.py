import uuid
from time import sleep
from redis import Redis, ConnectionPool

pool = ConnectionPool(host='0.0.0.0', port=6379, db=0)
conn = Redis(connection_pool=pool)

while True:
    conn.publish('main', f'Message {uuid.uuid4()}')
    sleep(1)
