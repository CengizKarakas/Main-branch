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
def send_config_commands(devices, commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']}")
        output = connection.send_config_set(commands)
        print(f"Configuration output from {device['ip']}:\n{output}\n")
        connection.disconnect()
        
send_config_commands(devices, ['interface GigabitEthernet0/1', 'shutdown'])
