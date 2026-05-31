# AI Diagnostics System

## Overview

AI-diagnostics-system is a Python-based Linux system monitoring and incident analysis tool. It collects real-time CPU usage, memory statistics, and system logs, then sends the data to a local AI model for automated analysis and troubleshooting suggestions.

The goal of this project is to simulate a lightweight AI-powered system administrator that can help detect and explain potential system issues.

---

## Features

* Collects top CPU-consuming processes
* Retrieves system memory usage
* Fetches recent system logs using `journalctl`
* Sends collected data to a local AI model (Ollama or similar)
* Generates:

  * Problem diagnosis
  * Severity level (Low / Medium / High)
  * Likely cause
  * Suggested fixes

---

## Requirements

* Python 3.x
* Linux system (recommended for `journalctl`)
* `requests` library
* Local AI server (example: Ollama running at `http://localhost:11434`)

Install dependencies:

```bash
pip install requests
```

---

## Usage

Run the script:

```bash
python3 AI-diagnostics-system.py
```

---

## How It Works

1. The script collects system data:

   * CPU usage (`ps aux`)
   * Memory usage (`free -h`)
   * Recent logs (`journalctl`)

2. It formats the data into a structured prompt.

3. The prompt is sent to a local AI model via HTTP POST request.

4. The AI returns an analysis including:

   * What is wrong
   * Severity level
   * Likely cause
   * Fix steps

---

## Example Output

```
1. What is wrong: High CPU usage detected in multiple processes
2. Severity: Medium
3. Likely cause: Background stress processes or runaway script
4. Fix steps: Identify and kill high CPU processes using kill <PID>
```

---

## Notes

* This project requires a running local AI model (Ollama recommended).
* Ensure `journalctl` is available on your system.
* If logs fail to load, run with sudo privileges.

---

## Purpose

This project was built for learning:

* Linux system monitoring
* Process management
* API communication with local AI models
* Basic AI-assisted system diagnostics
