import subprocess 
import requests
import psutil
import time

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
-High CPU usage by "ollama" is normal during AI inference.
-Do NOT treat high ollama CPU as an error condition.
-If a process name is "yes", "stress", or "stress-ng", treat it as an intentional CPU stress test unless stated otherwise.
-Only consider it a problem if CPU is high AND the process is stuck or not responding for a long time.
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

    response = requests.post("http://localhost:11434/api/generate", json={"model": "llama3", "prompt": prompt, "stream": False})
    print(response.json()["response"])

if __name__ == "__main__":

	while True:

		cpu_percent = psutil.cpu_percent(interval=1)
		memory_percent = psutil.virtual_memory().percent

		print(f"CPU: {cpu_percent}% | "f"Memory: {memory_percent}%"
    		)

    	# Trigger AI only if something looks wrong
		if cpu_percent > 90 or memory_percent > 85:
			print("\nALERT: Threshold exceeded.")
			print("Collecting evidence and consulting AI...\n")

			data = obtain_system_data()

			analyze_with_assistant(data)

			time.sleep(300)

		elif cpu_percent > 50 or memory_percent > 50:

       			print("\nALERT: SYSTEM HAS REACHED HALF OF THE THRESHOLD.")
       			print("Collecting evidence and consulting AI...\n")

       			data = obtain_system_data()

       			analyze_with_assistant(data)

        	# Cooldown period
       			time.sleep(300)

		else:
        		print("System operating normally.")

		time.sleep(60)


