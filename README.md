# shakeel_mac_changer
A mac address changer script in python

# Usage: mac_changer.py

# Syntax:
  python mac_changer.py -i <interface_name> -m <new_mac_address>
  // run the ifconfig command to get your interface and network details
  
# Example:
  python mac_changer.py -i eth0 -m 00:11:22:33:44:55

# Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change it's MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
  
