import sys
		
print("-----------------")
print("-----------------")
print("Phase1-Proposal")
print("-----------------")
print("-----------------")

nafn = input("Nafn a tengingu : ")
interface = input("Interface(incoming) : ")
keylife = input("Keylife(t.d. 3600) : ")
encrypt = input("Encryption(t.d. 3des) : ")
authentication = input("Authentication(md5 o.sv.fr) : ")
diffie = input("Diffie-Hellman group : ")
remoteserver = input("Remote server : ")
preshared = input("Pre-shared key : ")


set_name = "edit "+nafn
set_interface = "    set interface "+interface
set_keylife = "    set keylife "+keylife
set_proposal = "    set proposal "+encrypt+"-"+authentication
set_diffie = "    set dhgrp "+diffie
set_remoteserver = "    set remote-gw "+remoteserver
set_preshare = "    set psksecret "+preshared

print("-----------------")
print("-----------------")
print("Phase2-Selectors")
print("-----------------")
print("-----------------")

encrypt2 = input("Encryption(t.d. 3des) : ")
authentication2 = input("Authentication(md5 o.sv.fr) : )")
diffie2 = input("Diffie-Hellman group : ")
keylife2 = input("Keylife(t.d. 3600) : ")

set_proposal2 = "    set proposal "+encrypt2+"-"+authentication
set_diffie2 = "    set dhgrp "+diffie2
set_keylife2 = "    set keylifeseconds "+keylife2



src_subnet_list = []
dst_subnet_list = []

phase1 = "config vpn ipsec phase1-interface"
phase2 = "config vpn ipsec phase2-interface"

ask1 = "yes"
ask2 = "yes"

while ask2 !="no":
	src_subnet = input("src subnet :")
	ask2 = input("Villtu sla inn annad src subnet? (yes/no)")
	
	dst_subnet_list.append(src_subnet)

while ask1 !="no":
	dst_subnet = input("dst subnet : ")
	ask1 = input("Villtu sla inn annad dstsubnet? (yes/no)")
	
	src_subnet_list.append(dst_subnet)

print(phase1+"\n"+set_name,"\n"+set_interface,"\n"+set_keylife+"\n"+set_proposal,"\n"+set_diffie,"\n"+set_remoteserver+"\n"+set_preshare+"\n""end")

count = 0
for k in src_subnet_list:
	for i in dst_subnet_list:
		print(phase2)
		print("edit "+nafn+"-"+str(count))
		print("    set phase1name "+nafn)
		print(set_proposal2)
		print(set_diffie2)
		print(set_keylife2)
		print("    set src-subnet "+k)
		print("    set dst-subnet "+i)
		print("end")
		count += 1

