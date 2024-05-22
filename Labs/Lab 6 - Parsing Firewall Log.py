"""
1. Parse the Lab 6: Log File.txt file

2. Print each data field with a description ex: "Source IP: 192.168.1.1"​

3. Bonus: How many SSH destination sites were blocked
"""

# Counting the bonus step 3
bonusStep = 0 

#2024-01-29 14:50:00,10.0.0.9,INTERNAL,ALLOW,inbound,web4.example.com
with open('Labs/Lab 6 - Log File.txt', 'r') as file:
    for line in file:
        fields = line.strip().split(',')
        if len(fields) == 6:
            timestamp, source_ip, zone, action, direction, destination = fields
            if action == "DENY" and "ssh" in destination:
                bonusStep +=1
            print("Timestamp:", timestamp)
            print("Source IP:", source_ip)
            print("Zone:", zone)
            print("Action:", action)
            print("Direction:", direction)
            print("Destination:", destination)
            print()
        else:
            print("Invalid log entry:", line)

print(f"There were {bonusStep} logs entries that were SSH destination and Blocked\n")