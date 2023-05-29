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
# Run show commands and save the output
def run_show_commands_and_save(devices, commands, output_dir):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']}")
        output = connection.send_command(commands)
        file_name = f"{output_dir}/{device['ip']}_output.txt"
        with open(file_name, 'w') as file:
            file.write(output)
        print(f"Saved output from {device['ip']} to {file_name}\n")
        connection.disconnect()
        
run_show_commands_and_save(devices, 'show interfaces', 'output_directory')
