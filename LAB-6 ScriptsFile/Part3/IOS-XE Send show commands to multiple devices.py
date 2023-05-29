from netmiko import ConnectHandler

# Define the device information
devices = [
    {
        'device_type': 'cisco_xe',
        'ip': '10.125.100.187',
        'username': 'admin',
        'password': 'pxl',
    },
    {
        'device_type': 'cisco_xe',
        'ip': '10.125.100.181',
        'username': 'admin',
        'password': 'pxl',
    },
    
]
# Connect to multiple devices and send show commands
def send_show_commands(devices, commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']}")
        output = connection.send_command(commands)
        print(f"Output from {device['ip']}:\n{output}\n")
        connection.disconnect()
        
 send_show_commands(devices, 'show interfaces')
