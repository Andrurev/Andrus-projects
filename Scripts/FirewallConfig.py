# Import the required libraries
import subprocess

# Set the network interface
interface = "eth0"

# Set the default policy
subprocess.run(["iptables", "-P", "INPUT", "DROP"])
subprocess.run(["iptables", "-P", "OUTPUT", "ACCEPT"])
subprocess.run(["iptables", "-P", "FORWARD", "DROP"])

# Allow incoming SSH connections
subprocess.run(["iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--dport", "22", "-m", "state", "--state", "NEW,ESTABLISHED", "-j", "ACCEPT"])
subprocess.run(["iptables", "-A", "OUTPUT", "-o", interface, "-p", "tcp", "--sport", "22", "-m", "state", "--state", "ESTABLISHED", "-j", "ACCEPT"])

# Allow outgoing HTTP and HTTPS connections
subprocess.run(["iptables", "-A", "OUTPUT", "-o", interface, "-p", "tcp", "--dport", "80", "-m", "state", "--state", "NEW,ESTABLISHED", "-j", "ACCEPT"])
subprocess.run(["iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--sport", "80", "-m", "state", "--state", "ESTABLISHED", "-j", "ACCEPT"])
subprocess.run(["iptables", "-A", "OUTPUT", "-o", interface, "-p", "tcp", "--dport", "443", "-m", "state", "--state", "NEW,ESTABLISHED", "-j", "ACCEPT"])
subprocess.run(["iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--sport", "443", "-m", "state", "--state", "ESTABLISHED", "-j", "ACCEPT"])

# Allow incoming DNS queries
subprocess.run(["iptables", "-A", "INPUT", "-i", interface, "-p", "udp", "--dport", "53", "-m", "state", "--state", "NEW,ESTABLISHED", "-j", "ACCEPT"])
subprocess.run(["iptables", "-A", "OUTPUT", "-o", interface, "-p", "udp", "--sport", "53", "-m", "state", "--state", "ESTABLISHED", "-j", "ACCEPT"])

# Save the firewall rules
subprocess.run(["service", "iptables", "save"])
This script uses the subprocess library to run the iptables command to configure the firewall rules. It sets the default policy to drop incoming and forward packets, and then adds rules to allow incoming SSH connections, outgoing HTTP and HTTPS connections, and incoming DNS queries. It also saves the firewall rules so that they persist after a reboot.

You can modify the script to add additional rules for different network services
