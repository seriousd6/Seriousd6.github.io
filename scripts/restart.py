#!/usr/bin/env python3
"""Restart the local dev server. Run from anywhere: python3 scripts/restart.py [port]"""
import os, signal, subprocess, sys
import psutil

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = '/tmp/bsw-server.log'

# Kill any process already listening on the port
for proc in psutil.process_iter(['pid', 'connections']):
    try:
        for conn in proc.connections():
            if conn.laddr.port == PORT:
                print(f'Stopping PID {proc.pid} on port {PORT}...')
                proc.send_signal(signal.SIGKILL)
                break
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

print(f'Starting server at http://localhost:{PORT}')
with open(LOG, 'w') as log:
    p = subprocess.Popen(
        [sys.executable, 'scripts/serve.py', str(PORT)],
        cwd=REPO_ROOT, stdout=log, stderr=log,
        start_new_session=True,
    )
print(f'PID {p.pid} — logs at {LOG}')
