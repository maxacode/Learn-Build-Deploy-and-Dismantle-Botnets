"""
1. Set up a dictionary with services and their port numbers. 
2. Create a statement that asks the user for a service name. 
3. Print the specified service and port number.
"""
# Dictionary of services and their port numbers
services = {
    "http": 80,
    "https": 443,
    "ftp": 21,
    "ssh": 22,
    "smtp": 25,
    "dns": 53 }
# Ask the user for a service name
counter = 0 
while counter < 3:
    service_name = input("Enter a service name or exit to close: ")
    # Check if the service name exists in the dictionary
    counter += 1
    if service_name == "exit":
        break
    if service_name in services:
        print("Service:", service_name)
        print("Port number:", services[service_name])
    else:
        print("Service not found.")
