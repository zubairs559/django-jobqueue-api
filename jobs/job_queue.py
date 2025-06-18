import threading
import uuid
import time

# In-memory store
jobs_store = {}
lock = threading.Lock()

def process_job(job_id, payload):
    """ Simulate a job (e.g., long-running task) """
    time.sleep(5)  # Simulate delay

    result = f"Processed payload: {payload}"

    with lock:
        jobs_store[job_id]['status'] = 'completed'
        jobs_store[job_id]['result'] = result


def add_job(payload):
    job_id = str(uuid.uuid4())
    with lock:
        jobs_store[job_id] = {
            'status': 'queued',
            'result': None,
            'payload': payload
        }

    thread = threading.Thread(target=process_job, args=(job_id, payload))
    thread.start()

    return job_id


def get_job_status(job_id):
    with lock:
        return jobs_store.get(job_id, None)
