# Detection System

## Overview

Detection_system.sh is a Bash-based system monitoring and failure simulation project. The script generates CPU and memory stress, creates simulated log events, and demonstrates basic incident detection and troubleshooting techniques in a Linux environment.

## Features

* Simulates CPU stress using background processes
* Generates memory load using the stress utility
* Creates sample system log entries with logger
* Demonstrates process identification using PIDs
* Provides guidance for terminating resource-intensive processes

## Requirements

* Linux
* Bash
* stress package
* systemd-journald (for log monitoring)

## Usage

Make the script executable:

```bash
chmod +x Detection_system.sh
```

Run the script:

```bash
./Detection_system.sh
```

## Learning Objectives

This project was created to practice:

* Linux process management
* System monitoring
* Resource utilization analysis
* Log generation and analysis
* Basic cybersecurity and system administration concepts
