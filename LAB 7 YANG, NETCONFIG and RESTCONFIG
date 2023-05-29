Part 1: Install the CSR1000v VM
Lab netacad: Cisco DEVNET 7.0.3

Task preparation and implementation:
To download the CSR1000v ISO go to:
  https://software.cisco.com/download/home/284364978/type/282046477/release/Fuji-16.9.5
Navigate to the DevNet Associate Virtual Machines (VMs) page on netacad.com.
Download the DEVASC_CSR1000v.zip and note the location of file. 
PXL students can download both files from this link.
  https://hogeschoolpxl-my.sharepoint.com/personal/20003844_pxl_be/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F20003844%5Fpxl%5Fbe%2FDocuments%2FENTERPRISE%20NETWORKS%201%20%2D%20SHARED%2FTools&ga=1
In VMware, select the file CSR1000v_for_VMware.ova and click Open > import
Select the CSR1000v VM and click Start or Power On
Attached to: Host-only Adapter > click OK
  CSR1kv> enable
  CSR1kv# show ip interface brief
 Open a terminal
  devasc@labvm:~$ ping 10.176.177.73
  devasc@labvm:~$ ssh cisco@10.176.177.73
Open a web browser on the DEVASC VM.
 For the URL enter: https://10.176.177.73
If your browser displays a warning similar to, “Your connection is not private”:
  Click Advanced> Click Proceed to 10.176.177.73 (unsafe).
  You will now see a LOGIN screen. Enter the following: Username: cisco | Password: cisco123! > Click LOGIN NOW.  
Task troubleshooting:
-
Task verification:  
  You can find the screenshots in the LAB-7 Poto's file.

Part 2: Explore YANG Models
Lab netacad: Cisco DEVNET 8.3.5

Task preparation and implementation:
  Open Chromium and navigate to https://github.com/YangModels/yang.
  Under master branch > vendor > cisco > xe > 1693 > ietf-interfaces.yang.
  devasc@labvm:~/labs/devnet-src$ mkdir pyang
  devasc@labvm:~/labs/devnet-src/pyang$ wget https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1693/ietf-interfaces.yang
  devasc@labvm:~/labs/devnet-src$ pyang -v;
  devasc@labvm:~/labs/devnet-src$ pip3 install pyang --upgrade
  devasc@labvm:~/labs/devnet-src/pyang$ pyang -h | more
  devasc@labvm:~/labs/devnet-src/pyang$ pyang -f tree ietf-interfaces.yang
Task troubleshooting:
-
Task verification:  
  You can find the screenshots in the LAB-7 Poto's file.
  
Part 3: Use NETCONF to Access an IOS XE Device
Lab netacad: cisco DEVNET 8.3.6
  From your SSH session with the CSR1kv, use the "show platform software yang-management process" command to see if the NETCONF SSH daemon (ncsshd) is running.
  CSR1kv (config)# netconf-yang
  devasc@labvm:~$ ssh cisco@10.176.160.175 -p 830 -s netconf
  CSRk1v# show netconf-yang sessions
Task troubleshooting:
-
Task verification:  
  You can find the screenshots in the LAB-7 Poto's file.
Part 4: Use RESTCONF to Access an IOS XE Device
Lab netacad: cisco DEVNET 8.3.7

Task preparation and implementation:
Task troubleshooting:
Task verification:
