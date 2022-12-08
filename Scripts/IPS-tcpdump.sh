#!/bin/bash

# Capture packets on the network interface
tcpdump -i eth0 -n -c 100 > /tmp/packets.txt

# Loop through the captured packets
while read line; do
    # Parse the TCP flags
    flags=$(echo $line | grep "Flags" | awk '{print $6}')

    # Check for potential attacks
    if [[ $flags == "SYN" ]]; then
        # Block the attacker's IP address
        ip=$(echo $line | grep "IP" | awk '{print $3}')
        iptables -A INPUT -s $ip -j DROP
        echo "Blocked $ip for SYN flood attack"
    elif [[ $flags == "FPU" ]]; then
        # Block the attacker's IP address
        ip=$(echo $line | grep "IP" | awk '{print $3}')
        iptables -A INPUT -s $ip -j DROP
        echo "Blocked $ip for XMAS tree attack"
    # ...
done < /tmp/packets.txt
This script uses the tcpdump command to capture packets on the eth0 network interface, and then saves the captured packets to a temporary file. It then reads the packets from the file and uses the grep and awk commands to parse the TCP flags. If an attack is detected, the script uses the iptables command to block the attacker's IP address.

You can modify the script to add additional checks for different attack patterns, and to take different actions when an attack is detected. For example, you could add code to send an email or text message alert, or to use a different method for blocking IP addresses.
