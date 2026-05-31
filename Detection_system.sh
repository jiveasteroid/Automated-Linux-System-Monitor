#!/bin/bash

echo ""
echo "Failure Detection system in progress.."

#Spams Y and discards them. Also stores a background process.
echo ""
yes > /dev/null &
CPU_PID=$!

#CPU is stressed and prints out the process causing the issue.
echo ""
echo "CPU stressed: PID $CPU_PID"

#Pause for 5 secs.
echo ""
sleep 5

#Runs the for loop 5 times(1,2,3,4,5) and starts a memory worker(vm). The vm uses 200 megabytes of memory then timesout after 10 seconds and runs this in the background until done.
echo ""
for i in {1..5}; do
  stress --vm 1 --vm-bytes 200M --timeout 10s &
done

echo "Memory Stressed"

#Log errors for project. Sends messages to the logging system.
echo ""
logger "ERROR: Database connection down"
logger "WARNING: High latency detected"
logger "ERROR: Disk response timeout"

#Sleeps for 10 seconds.
echo ""
sleep 10
#Detection system suggest to kill the process causing the problem.
echo ""
echo "Detection system running. Halt CPU stress with: kill $CPU_PID"





