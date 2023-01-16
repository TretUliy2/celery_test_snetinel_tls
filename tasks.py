import os
import ssl

from redis.sentinel import SentinelManagedSSLConnection

from celery import Celery

HOST = os.environ.get("REDIS_HOST", "localhost")
broker_url = 'sentinel://:password@sentinel1:26379;sentinel://sentinel2:26379;sentinel://sentinel3:26379'
backend_url = 'sentinel://:password@sentinel1:26379;sentinel://:password@sentinel2:26379;sentinel://:paswword@sentinel3:26379'

redis_backend_use_ssl = {
    'ssl_cert_reqs': ssl.CERT_REQUIRED,
    'ssl_ca_certs': '/etc/redis/ssl/ca.crt'
}

app = Celery('tasks', broker=broker_url, backend=backend_url, redis_backend_use_ssl=redis_backend_use_ssl, broker_use_ssl=redis_backend_use_ssl)
app.conf.broker_transport_options = { 'master_name': "mymaster" }
app.conf.result_backend_transport_options = { 'master_name': "mymaster" }

@app.task
def add(x, y):
    print("Will return x + y")
    return x + y
