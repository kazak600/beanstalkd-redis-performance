from redis import Redis, ConnectionPool

pool = ConnectionPool(host='0.0.0.0', port=6379, db=0)
conn = Redis(connection_pool=pool)

sub = conn.pubsub()
sub.subscribe('main')
for message in sub.listen():
    print(message)
