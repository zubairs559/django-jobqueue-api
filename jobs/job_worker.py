import threading
import queue
import time

job_queue = queue.Queue()
job_results = {}

def worker():
    while True:
        job_id, payload = job_queue.get()
        if job_id is None:
            break  # Graceful shutdown
        print(f"Processing job {job_id} with payload: {payload}")
        time.sleep(3)  # Simulate long task
        job_results[job_id] = f"Processed: {payload}"
        job_queue.task_done()

# Start worker thread
threading.Thread(target=worker, daemon=True).start()

def add_job(job_id, payload):
    job_queue.put((job_id, payload))