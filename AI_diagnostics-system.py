import subprocess 
import requests

#Obtains CPU, Memory, Logs.
def obtain_system_data():
    cpu = subprocess.getoutput("ps aux --sort=-%cpu | head -5")
    memory = subprocess.getoutput("free -h")
    logs = subprocess.getoutput("journalctl -n -10 --no-pager")

    return f"""
CPU Process list:
{cpu}

Memory:
{memory}

Recent Logs:
{logs}
"""
def analyze_with_assistant(data):
    prompt = f"""
You are a Linux incident analyst.

RULES:
-Don't guess time duration.
-CPU_TIME means total process CPU usage , NOT system history.
-Only use data provided.
-If something is uknown, say "Not enough data" 
Analyze this system's data:
{data}

Return:
1. What is wrong
2. Severity (Low/Medium/High)
3. Likely cause
4. Fix steps

Data provided:
{data}
"""

    response = requests.post("http://localhost:11434/api/generate", json={ "model": "llama3", "prompt": prompt, "stream": False})

    print(response.json()["response"])

if __name__ == "__main__":
    data = obtain_system_data()
    analyze_with_assistant(data)
