#!/bin/bash

echo "==============================="
echo "System Monitor"
echo "==============================="

#Runs for top 5 CPUs.
echo ""
echo "CPU"
top -bn1 | head -5

#Sorts top 5 live processes.
echo ""
echo "Top Processes"
ps aux --sort=-%cpu | head -5

echo ""
echo "Memory"
free -h

echo ""
echo "Disk Usage"
df -h | head -5

#10 most recent log entries.
echo ""
echo "Recent Logs"
journalctl -n 10 --no-pager 

echo ""
echo "======== $(date) ========"

echo ""
echo "Done checking system"



