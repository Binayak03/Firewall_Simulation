import random 
import ipaddress

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def check_firewall_rule(ip, firewall_rules):
    ip = ipaddress.ip_address(ip)
    for network in firewall_rules["blocked_ips"]:
        if ip in network:
            return "Blocked IP"
    if ip in firewall_rules["malicious_ips"]:
        return "Malicious IP"
    if ip in firewall_rules["suspicious_ips"]:
        return "Suspicious IP"
    return "Allowed IP"

def main():
    firewall_rules = {
        "blocked_ips": [
            ipaddress.ip_network("169.233.0.0/16"),
            ipaddress.ip_network("10.0.0.0/8"), 
            ipaddress.ip_network("172.16.0.0/12"),  
            ipaddress.ip_network("192.168.0.0/16")
        ],
        "malicious_ips": {
            ipaddress.ip_address("45.155.205.99"),
            ipaddress.ip_address("185.220.101.1"),
            ipaddress.ip_address("103.81.214.226"),
            ipaddress.ip_address("198.96.155.3"),
        },
        "suspicious_ips": {
            ipaddress.ip_address("66.240.236.119"),
            ipaddress.ip_address("209.126.136.4"),
            ipaddress.ip_address("162.247.74.200"),
        }
    }

    print(f"{'IP Address':<18} {'Action':<18} {'Random ID':<10}")
    print("-" * 50)

    for _ in range(500):
        rand_value = random.random()

        if rand_value < 0.05:
            ip_address = str(random.choice(list(firewall_rules["malicious_ips"])))
        elif rand_value < 0.10:
            ip_address = str(random.choice(list(firewall_rules["suspicious_ips"])))
        else:
            ip_address = generate_random_ip()  # Only generate if no known IP injected

        action = check_firewall_rule(ip_address, firewall_rules)
        random_number = random.randint(1, 9999)
        print(f"IP Address: {ip_address:<18} - Action: {action:<15} Random ID: {random_number:<10}")

if __name__ == "__main__":
    main()
