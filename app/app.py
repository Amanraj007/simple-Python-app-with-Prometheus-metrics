from flask import Flask
import time, random
from prometheus_client import start_http_server, Counter, Histogram

app = Flask(__name__)
REQUESTS = Counter('sample_app_requests_total', 'Total app requests')
LATENCY = Histogram('sample_app_request_latency_seconds', 'Request latency')

@app.route("/")
@LATENCY.time()
def hello():
    REQUESTS.inc()
    time.sleep(random.random() * 0.2)
    return "Hello from Sample App!\n"

if __name__ == "__main__":
    start_http_server(8000)   # Prometheus metrics on :8000/metrics
    app.run(host="0.0.0.0", port=5000)

