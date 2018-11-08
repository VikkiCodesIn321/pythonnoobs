#!usr/bin/python

from pexpect import pxssh
import pexpect
import sys
import time
import socket

ssh = pxssh.pxssh()

def cli_return():
	'''Outputs CLI readout'''
	ssh.prompt()
	cli_output = ssh.before.decode("utf-8").split("\r\n")[1:]
	return "\n".join(map(str,cli_output))
def sw_fp_login():
	ssh.sendline("telnet localhost")
	ssh.sendline("en")
def fw_group():
	'''Function for iptables chains'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		#ssh.sendline("show firewall name ?")
		#names_return = cli_return()
		#print(names_return)
		chain = input("Which iptables chain would you like to query? ").upper()
		print("Let me get that for you. Loading...")
		#if chain.upper() != "LAN_IN" or "WAN_IN":
			#raise ValueError("Must be a valid iptables chain")
		ssh.sendline("sudo iptables -L {} -v".format(chain))
		fw_return = cli_return()
		print(fw_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def rt():
	'''Function for routing table'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Let me get that for you. Loading...")
		ssh.sendline("show ip route")
		rt_return = cli_return()
		print(rt_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def arp():
	'''Function for routing table queries'''
	ssh.sendline("show interfaces ethernet")
	cli_return()
	arp_int = input("Which interface would you like to see ARP entries for? ").lower()
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Let me get that for you. Loading...")
		ssh.sendline("show arp {} | no-more".format(arp_int))
		arp_return = cli_return()
		print(arp_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def vpn():
	'''Function for VPN SA'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Let me get that for you. Loading...")
		ssh.sendline("show vpn ipsec sa")
		vpn_return = cli_return()
		print(vpn_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def ping():
	'''Ping tool'''
	ping_trg = input("What is the IP address that you would like to ping? ")
	ping_ct = int(input("How many times would you like the ICMP packet sent? "))
	#ping_sz = input("What size ICMP packets would you like? (Default: 56 bytes) ")
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Please hold while this test completes with {}x ICMP packets...".format(ping_ct))
		for i in range(ping_ct):
			ssh.sendline("sudo ping -s 56 {} -c 1".format(ping_trg))
			ping_return = cli_return()
			for line in ping_return.split("\n"):	
				if "ttl=" in line:
					print(line)
					time.sleep(0.2)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def mac_addr_table():
	'''Function to query switch MAC address table'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Let me get that for you. Loading...")
		sw_fp_login()
		ssh.sendline("show mac-addr-table")
		#for i in range(1):
		ssh.sendline(" ")
		mac_return = cli_return()
		print(mac_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def danger():
	sw_fp_login()
	ssh.sendline("show ?")
	sw_show_list = cli_return()
	while "--More-- or (q)uit" in sw_show_list:
		ssh.sendline(" ")
		print("Still working...")
	print(sw_show_list)
	input("what is this lol")
def trcrt():
	'''Function for traceroute'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		tr_host = input("Which IP would you like to target for traceroute? ")
		print("Please hold while this test completes...")
		ssh.sendline("traceroute {}".format(tr_host))
		trcrt_return = cli_return()
		print(trcrt_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def exit():
	'''Function for exiting'''
	ssh.logout()
	print("Thanks for trying this out!")
def pmtud():
	'''PMTUD function'''
	#seg_size = int(input("What segment size would you like to try? (Number between 1 and 1500) "))
	seg_size = 1500
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Please hold while this test completes...")
		ssh.sendline("sudo ping -s {} -M do www.google.com -c 1".format(seg_size))
		pmtud_return = cli_return() 
		while 'Frag needed' in pmtud_return:
			seg_size -= 1
			ssh.sendline("sudo ping -s {} -M do www.google.com -c 1".format(seg_size))
			good_seg = cli_return()
			#print("\n"+str(seg_size + 1)+" is too large of a segment size!") 
			if "ttl=" in good_seg:
				print("\n" + str(seg_size) + " is a perfect segment size for your network.")
				break
		else:
			print("\n"+str(seg_size) + " is a perfect segment size for your network.")
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def info():
	'''MCAD Info'''
	if not login:
		print("SSH Unsuccessful")
		print(str.ssh)
	else:
		print("Getting info status for you. Please hold...")
		ssh.sendline("info")
		info_return = cli_return()
		print(info_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
def pbr():
	'''PBR definition work in progress'''
	if login:
		source_net = input("What is the source IP or network or host that you want to policy route? (netmask must be included) ")
		next_hop = input("What is the next hop IP of your desired path? ")
		int_placement = input("Which interface should this modify rule be placed on? (eth1,eth2,etc) ")
		print("set protocols static table 5 route 0.0.0.0/0 next-hop {}".format(next_hop))
		print("set firewall modify LOAD_BALANCE rule 2501 action modify")
		print("set firewall modify LOAD_BALANCE rule 2501 protocol all")
		print("set firewall modify LOAD_BALANCE rule 2501 modify table 5")
		print("set firewall modify LOAD_BALANCE rule 2501 source address {}".format(source_net))
		print("set interfaces ethernet {} firewall in modify VPN_Gateway".format(int_placement))
		print("\nEnd of Commands\n")
		input("Press Enter to continue...")
	else:
		print("SSH Unsuccessful")
		print(str.ssh)
def conntrack():
	'''connection tracking table output'''
	if login:
		source_ip = input("Which source IP would you like to see connection tracking information for? ")
		print("Getting connection tracking information for {}. Please hold...".format(source_ip))
		ssh.sendline("show conntrack table ipv4 source {} | no-more".format(source_ip))
		conntrack_return = cli_return()
		print(conntrack_return)
		print("\nEnd of query\n")
		input("Press Enter to continue...")
	else:
		print("SSH Unsuccessful")
		print(str.ssh)	
#End of Functions

#Start of inputs
while True:	
	dev_list = ["USW", "USG", "", "exit"]
	print("\n".join(map(str,dev_list)))
	dev_type = input("Which type of device would you like to query? ")
	func_list_usg = ["iptables chains","routing table","arp table","vpn sa", "icmp","traceroute","pmtud testing","info","pbr commands","conntrack table"," ","exit"]
	func_list_usw = ["mac-addr-table","icmp","traceroute","info","danger (dont use this)"," ","exit"]	
	if dev_type.upper() == "USG":
		dev_ip = input("What is the IP of your device? ")
		uname = input("What is your username on the device with the IP of " + dev_ip +"? ")
		pwd = input("What is your password on the device with the IP of " + dev_ip +"? (Optional if you use keys) ")
		login = ssh.login(dev_ip,uname,pwd)
		while True:
			print("USG Command Catalogue")
			print("----------------------------")
			print("\n".join(map(str,func_list_usg)))
			selection = input("Which would you like to query? ").lower()
			if selection == func_list_usg[0]:
				fw_group()
			elif selection == func_list_usg[1]:
				rt()
			elif selection == func_list_usg[2]:
				arp()
			elif selection == func_list_usg[3]:
				vpn()
			elif selection == func_list_usg[4]:
				ping()
			elif selection == func_list_usg[5]:
				trcrt()
			elif selection == func_list_usg[6]:
				pmtud()
			elif selection == func_list_usg[7]:
				info()
			elif selection == func_list_usg[8]:
				pbr()
			elif selection == func_list_usg[9]:
				conntrack()
			else:
				ssh.logout()
				ssh.close()
				break
	elif dev_type.upper() == "USW":
		dev_ip = input("What is the IP of your device? ")
		uname = input("What is your username on the device with the IP of " + dev_ip +"? ")
		pwd = input("What is your password on the device with the IP of " + dev_ip +"? ")
		login = ssh.login(dev_ip,uname,pwd)
		while True:
			print("Switch Command Catalogue")
			print("----------------------------")
			print("\n".join(map(str,func_list_usw)))
			selection = input("Which would you like to query? ").lower()
			if selection == func_list_usw[0]:
				mac_addr_table()
			elif selection == func_list_usw[1]:
				ping()
			elif selection == func_list_usw[2]:
				trcrt()
			elif selection == func_list_usw[3]:
				info()
			elif selection == func_list_usw[4]:
				danger()
			else:
				break
				ssh.logout()
				ssh.close()
	elif dev_type.lower() == "exit":
		print("Thanks for trying this out!!")
		raise SystemExit
		ssh.logout()
		ssh.close()