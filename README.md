**Firewall Simulation Project**
This project is made to simulate the working of firewall by randomly generating the ip addresses. It checks each generated ips and take actions according to the rule.

## What does it do ?
- Generates IPs
- Check them according to the rule
- Blocks IPs (Based on Ip range)
- Shows Malicious IPs
- Shows Suspicious IPs
- Allows IP that are not against the rules.
- Injects known malicious/ suspicious IPs with a configurable probability.
- outputs a log with IP, action taken, and rando IP ID.
- Clean formated console output

  
## How to Run this code ??
1. Make sure python3 is installed
2. clone the repository into a file named firewall.py.
3. Run the script
   ````bash
   **      python firewall.py**

   
## Extra Dose of information:
1. You can choose your number of ips to be generated
2. Blocked Ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, etc.
3. Malicious IPs: Hand-picked list of known bad actors.
4. Suspicious IPs: Tor nodes, scanners (e.g., Shodan).

   
# Note:
This is not a real firewall but a simulation.
