#!/usr/bin/env python
import subprocess
import optparse
import re

should_terminate = False

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please provide an interface, use --help for more info")
    if not options.new_mac:
        parser.error("[-] Please provide a new mac, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface])
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read mac address")
            return ""
    except:
        print("[-] Please provide a valid interface")
        return ""


options = get_arguments()
current_mac = get_current_mac(options.interface)

if not current_mac == "":
    print("[+] Current MAC: " + str(current_mac))
    change_mac(options.interface, options.new_mac)
    current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print("[+] MAC address changed to " + str(current_mac))
else:
    print("[-] Cannot change MAC address")
