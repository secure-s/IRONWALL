#!/usr/bin/env python3
"""
Basic usage example for IRONWALL firewall
"""
from ironwall import Firewall, Rule, RuleAction


def main():
    print("=== IRONWALL Firewall Example ===\n")
    
    # Create a new firewall instance
    firewall = Firewall()
    print("Created firewall with default DENY policy")
    
    # Add some rules
    print("\nAdding firewall rules...")
    
    # Allow HTTP traffic
    firewall.add_rule(Rule(
        name="allow_http",
        action=RuleAction.ALLOW,
        port=80,
        protocol="TCP",
        priority=10
    ))
    print("✓ Added rule: Allow HTTP traffic on port 80")
    
    # Allow HTTPS traffic
    firewall.add_rule(Rule(
        name="allow_https",
        action=RuleAction.ALLOW,
        port=443,
        protocol="TCP",
        priority=10
    ))
    print("✓ Added rule: Allow HTTPS traffic on port 443")
    
    # Block traffic from specific IP
    firewall.add_rule(Rule(
        name="block_malicious_ip",
        action=RuleAction.DENY,
        source_ip="192.168.1.100",
        priority=20  # Higher priority
    ))
    print("✓ Added rule: Block all traffic from 192.168.1.100")
    
    # Allow SSH from specific IP
    firewall.add_rule(Rule(
        name="allow_admin_ssh",
        action=RuleAction.ALLOW,
        source_ip="10.0.0.5",
        port=22,
        protocol="TCP",
        priority=15
    ))
    print("✓ Added rule: Allow SSH from admin IP 10.0.0.5")
    
    # Test some packets
    print("\n" + "="*50)
    print("Testing Packets:")
    print("="*50)
    
    test_packets = [
        {
            "name": "HTTP Request",
            "packet": {"port": 80, "protocol": "TCP", "source_ip": "192.168.1.50"}
        },
        {
            "name": "HTTPS Request",
            "packet": {"port": 443, "protocol": "TCP", "source_ip": "10.0.0.10"}
        },
        {
            "name": "SSH from Admin",
            "packet": {"port": 22, "protocol": "TCP", "source_ip": "10.0.0.5"}
        },
        {
            "name": "Traffic from Blocked IP",
            "packet": {"port": 80, "protocol": "TCP", "source_ip": "192.168.1.100"}
        },
        {
            "name": "Unknown Port",
            "packet": {"port": 9999, "protocol": "TCP", "source_ip": "192.168.1.1"}
        }
    ]
    
    for test in test_packets:
        action, rule_name = firewall.check_packet(test["packet"])
        status = "✓ ALLOWED" if action == RuleAction.ALLOW else "✗ DENIED"
        rule_info = f" (by rule: {rule_name})" if rule_name else " (default policy)"
        print(f"\n{test['name']}: {status}{rule_info}")
        print(f"  Packet: {test['packet']}")
    
    # Show all rules
    print("\n" + "="*50)
    print("Current Firewall Rules:")
    print("="*50)
    for rule in firewall.list_rules():
        print(f"\n{rule}")
    
    print("\n" + "="*50)
    print("Example completed!")
    print("="*50)


if __name__ == "__main__":
    main()
