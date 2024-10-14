#!/bin/bash
# Use forward slashes for paths in Bash scripts on Windows
logfile="C:/Users/SURFACE PRO 4/remote_platform/job_platform/logfile.log"

# Create the directory for the log file if it doesn't exist
mkdir -p "$(dirname "$logfile")"

# Example command: append to the log file
echo "Running API job fetch at $(date)" >> "$logfile"

# Run your Django management command (fetch jobs)
python "C:/Users/SURFACE PRO 4/remote_platform/job_platform/manage.py" fetch_jobs >> "$logfile" 2>&1

# Add more commands as needed
