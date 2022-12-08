# Import the required libraries
use Net::Pcap;
use NetPacket::Ethernet qw(:strip);
use NetPacket::IP qw(:strip);
use NetPacket::TCP qw(:strip);

# Open a live capture on the network interface
my $pcap = Net::Pcap::open_live($interface, $snaplen, $promisc, $timeout);

# Set the packet filter
my $filter = 'tcp and port 80';
Net::Pcap::compile($pcap, \$filter_string, $filter, 0, 0);
Net::Pcap::setfilter($pcap, $filter_string);

# Set the packet callback function
Net::Pcap::loop($pcap, -1, \&process_packet, 0);

# Close the capture
Net::Pcap::close($pcap);

# Process each captured packet
sub process_packet {
    # Get the packet data
    my($user_data, $header, $packet) = @_;

    # Strip the Ethernet header
    my $eth_obj = NetPacket::Ethernet->decode(eth_strip($packet));

    # Strip the IP header
    my $ip_obj = NetPacket::IP->decode(ip_strip($eth_obj->{data}));

    # Strip the TCP header
    my $tcp_obj = NetPacket::TCP->decode(tcp_strip($ip_obj->{data}));

    # Check for potential attacks
    if ($tcp_obj->{flags} == 2) {
        print "SYN flood attack detected!\n";
    }
    elsif ($tcp_obj->{flags} == 18) {
        print "XMAS tree attack detected!\n";
    }
    # ...
}
This script uses the Net::Pcap library to capture packets on the specified network interface, and then uses the NetPacket::Ethernet, NetPacket::IP, and NetPacket::TCP libraries to decode the packet headers. It then checks for common network attack patterns in the TCP flags, and prints a message if an attack is detected.

You can modify the script to add additional checks for different attack patterns, and to take different actions when an attack is detected. For example, you could add code to send an email or text message alert, or to block the attacker's IP address.
