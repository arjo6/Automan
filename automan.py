import argparse
from modules import recon, exploit, priv_esc, shell, metasploit

def main():
    parser = argparse.ArgumentParser(description="Automan - Automated Penetration Testing Tool")
    parser.add_argument("--recon", help="Perform reconnaissance", action="store_true")
    parser.add_argument("--exploit", help="Run exploitation module", action="store_true")
    parser.add_argument("--priv-esc", help="Run privilege escalation", action="store_true")
    parser.add_argument("--shell", help="Generate and handle reverse shell", action="store_true")
    parser.add_argument("--metasploit", help="Automate Metasploit execution", action="store_true")

    args = parser.parse_args()

    if args.recon:
        recon.run()
    elif args.exploit:
        exploit.run()
    elif args.priv_esc:
        priv_esc.run()
    elif args.shell:
        shell.run()
    elif args.metasploit:
        metasploit.run()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
