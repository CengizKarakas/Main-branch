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
# Connect to a device and retrieve device information
def get_device_info(device):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")
    output = connection.send_command('show version')
    print(f"Device information from {device['ip']}:\n{output}\n")
    connection.disconnect()

# Send device configuration commands
def send_config_commands(device, commands):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")
    output = connection.send_config_set(commands)
    print(f"Configuration output from {device['ip']}:\n{output}\n")
    connection.disconnect()

# Execute advanced operations
def execute_advanced_operations(device):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")

    # Check interface status and shutdown interfaces with no traffic
    output = connection.send_command('show interfaces')
    for line in output.splitlines():
        if 'GigabitEthernet' in line and 'up' in line and 'up' not in line.split()[0]:
            interface = line.split()[0]
            print(f"Shutting down interface {interface}")
            connection.send_config_set(['interface ' + interface, 'shutdown'])

    # Execute additional advanced operations as needed
    # ...

    connection.disconnect()

# Usage examples
for device in devices:
    get_device_info(device)

config_commands = [
    'interface GigabitEthernet0/1',
    'ip address 10.125.100.187 255.255.255.0',
    'no shutdown',
]
send_config_commands(devices[0], config_commands)

execute_advanced_operations(devices[1])
