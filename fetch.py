"""
This file grabs a log from the roboRIO and copies it a local directory.

@author Arvind
"""

# Imports
from paramiko import SSHClient
from scp import SCPClient

# Declartion
ssh = SSHClient()

# Initialization
ssh.load_system_host_keys()
ssh.connect("172.22.11.2", "lvuser")

# Get log
with SCPClient(ssh.get_transport()) as scp:
    scp.get("~/log/test-log.log", "C:/Users/BUZZ-175/Development/RoboRIOLogs/test-log.log")