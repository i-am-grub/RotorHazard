"""
A server entry point
"""
import signal
import sys

from rotorhazard import server

if __name__ == "__main__":
    server.rh_program_initialize()
    signal.signal(signal.SIGINT, server.kill_server_via_signal)   # handle Ctrl-C signal
    signal.signal(signal.SIGTERM, server.kill_server_via_signal)  # handle kill-process signal
    server.start(argv_arr=sys.argv)