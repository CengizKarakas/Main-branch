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
# Backup device configurations
def backup_configurations(devices, backup_dir):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']}")
        output = connection.send_command('show running-config')
        file_name = f"{backup_dir}/{device['ip']}_config.txt"
        with open(file_name, 'w') as file:
            file.write(output)
        print(f"Saved configuration from {device['ip']} to {file_name}\n")
        connection.disconnect()
        
backup_configurations(devices, 'backup_directory')
