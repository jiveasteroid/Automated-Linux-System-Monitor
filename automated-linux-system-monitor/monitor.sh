#!/bin/bash

echo "==============================="
echo "System Monitor"
echo "==============================="

echo ""
echo "Running Processes"
ps aux | head -10

echo ""
echo "Top CPU Processes"
ps aux --sort=-%cpu | head -10

echo ""
echo "Memory"
free -h

echo ""
echo "Top Memory Processes"
ps aux --sort=-%mem | head -10

echo ""
echo "Disk Usage"
df -h | head -10 

echo ""
echo "======== $(date) ========"

echo ""
echo "Done checking system"



