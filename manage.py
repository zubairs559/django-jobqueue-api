#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import signal
from books.job_manager import job_threads



def graceful_shutdown(signum, frame):
    print("\n[⚠️  Graceful Shutdown] Waiting for background jobs to complete...")
    for thread in job_threads:
        if thread.is_alive():
            thread.join()
    print("[✅ Done] All jobs finished. Shutting down.")
    sys.exit(0)  # ✅ Add this line to actually stop Django



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    # ✅ Catch SIGINT (Ctrl+C) and SIGTERM
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
