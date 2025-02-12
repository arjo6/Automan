import subprocess

def run():
    print("[*] Running reconnaissance module...")
    target = input("Enter target domain or IP: ")
    
    print("[*] Running Nmap Scan...")
    subprocess.run(["nmap", "-A", "-T4", target])

    print("[*] Running Subdomain Enumeration (subfinder)...")
    subprocess.run(["subfinder", "-d", target])

    print("[+] Recon Completed.")
