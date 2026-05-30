# Automated Linux System Monitor

A Bash script that monitors system performance and logs key system information automatically.

## Features

- Displays running processes
- Shows top CPU-consuming processes
- Reports memory usage
- Shows top memory-consuming processes
- Reports disk usage
- Supports automation with cron jobs
- Logs system information for later review

## Technologies Used

- Bash
- Linux
- Cron
- Git

## How It Works

The script collects information about the system using Linux commands:

- `ps aux` – displays running processes
- `free -h` – displays memory usage
- `df -h` – displays disk usage

The script can be scheduled with cron to run automatically at regular intervals and save results to a log file.

## Usage

Make the script executable:

```bash
chmod +x monitor.sh
```

Run the script:

```bash
./monitor.sh
```

## Example Cron Job

Run every 5 minutes:

```bash
*/5 * * * * /path/to/monitor.sh >> monitor.log 2>&1
```

## What I Learned

- Bash scripting fundamentals
- Linux system monitoring commands
- File permissions and executable scripts
- Automating tasks with cron
- Version control with Git and GitHub

## Author

Michael Stewart
