#!/bin/bash

# Prompt for IP address
echo "Enter IP address: "
read ip_address

# Scan the IP address using nmap
nmap_output=$(nmap $ip_address)

# Extract the open ports from the nmap output
open_ports=$(echo "$nmap_output" | grep -oP '\d+(?=\/tcp.*open)' | tr '\n' ',' | sed 's/,$//')

# Print the open ports
echo "Open ports on $ip_address: $open_ports"
To use this script, save it to a file (e.g. nmap-scan.sh), make it executable with the command chmod +x nmap-scan.sh, and then run it with the command ./nmap-scan.sh. The script will prompt you for an IP address, and then display the open ports on the target host.



