import netifaces
import ipaddress

#.AF_LINK = mac, key 18
#.AF_INET = broadcast, netmask, ip
#.AF_INET6 = ipv6


def get_interfaces():
	inter = netifaces.interfaces()
	print(inter)
	return inter

def get_mac(interface: str):
	try:
		mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK]
		print("The mac address of "+interface+" is: "+str(mac))
		return mac
	except(KeyError):
		print("Does not have Mac Addr.")

def get_ips(interface: str):
	#look for key 'addr', this will be address in the 
	ip_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['addr']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have ipv4.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['addr']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have ipv6.")
	
	print(ip_dict)
	return ip_dict

def get_netmask(interface: str):
	#look for key 'addr', this will be address in the 
	nm_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['netmask']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have mask.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['netmask']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have mask.")
	
	print(nm_dict)
	return nm_dict

def get_network(interface: str):
	#look for key 'addr', this will be address in the 
	net_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['broadcast']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have network.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['broadcast']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have network.")
	
	print(net_dict)
	return net_dict

