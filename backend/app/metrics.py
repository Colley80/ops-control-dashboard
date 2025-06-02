# app/metrics.py

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Counter to track number of processes created
process_count = Counter('process_created_total', 'Total number of processes created')

def get_metrics():
    """Returns Prometheus metrics in proper format"""
    return generate_latest(), CONTENT_TYPE_LATEST
