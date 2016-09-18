import multiprocessing
import os

bind = '0.0.0.0:5000'
loglevel = 'debug'
timeout = 120
daemon = False
reload = True
workers = int(multiprocessing.cpu_count() * 2 + 1)
threads = int(multiprocessing.cpu_count())
errorlog = os.path.expanduser('logs/gunicorn_error.log')
accesslog = os.path.expanduser('logs/gunicorn_access.log')

if __name__ == '__main__':
    import sys

    sys.exit("""FATAL ERROR: This is configuratin file for gunicorn -
    `gunicorn -c gunicorn_cfg.py`""")
