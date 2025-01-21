"""Resolve hostnames concurrently, exit after 2 seconds.

Under the hood, this might use an asynchronous resolver based on
c-ares (the default) or thread-pool-based resolver.

You can choose between resolvers using GEVENT_RESOLVER environment
variable. To enable threading resolver:

    GEVENT_RESOLVER=thread python dns_mass_resolve.py
"""

import gevent

N = 1000
# limit ourselves to max 10 simultaneous outstanding requests
pool = gevent.pool.Pool(10)
finished = 0

def job(url):
    global finished
    try:
        try:
            ip = gevent.socket.gethostbyname(url)
            print('%s = %s' % (url, ip))
        except gevent.socket.gaierror as ex:
            print('%s failed with %s' % (url, ex))
    finally:
        finished += 1

with gevent.Timeout(2, False):
    for x in range(10, 10 + N):
        pool.spawn(job, '%s.com' % x)
    pool.join()

print('finished within 2 seconds: %s/%s' % (finished, N))