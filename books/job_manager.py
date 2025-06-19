import threading
import time
import uuid

# In-memory job store
job_store = {}
job_threads = []  # ✅ Track active threads

def job_function(job_id):
    try:
        time.sleep(10)  # Simulate long-running job
        job_store[job_id]["status"] = "completed"
    except Exception as e:
        job_store[job_id]["status"] = "failed"
        job_store[job_id]["error"] = str(e)

def create_job():
    job_id = str(uuid.uuid4())
    job_store[job_id] = {"status": "running"}
    thread = threading.Thread(target=job_function, args=(job_id,))
    thread.start()
    job_threads.append(thread)  # ✅ Add thread to global list
    return job_id
