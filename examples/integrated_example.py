#!/usr/bin/env python3
"""
Integrated example showing IRONWALL firewall and monitor working together
"""
from ironwall import Firewall, SecurityMonitor, Rule, RuleAction
from ironwall.monitor import SecurityEvent


def main():
    print("=== IRONWALL Integrated Security System ===\n")
    
    # Initialize components
    firewall = Firewall()
    monitor = SecurityMonitor()
    monitor.set_threat_threshold(2)
    
    print("Initialized firewall and security monitor")
    
    # Configure firewall rules
    print("\nConfiguring firewall rules...")
    firewall.add_rule(Rule(
        name="allow_web",
        action=RuleAction.ALLOW,
        port=80,
        priority=10
    ))
    firewall.add_rule(Rule(
        name="allow_secure_web",
        action=RuleAction.ALLOW,
        port=443,
        priority=10
    ))
    print("✓ Web traffic rules configured")
    
    # Simulate incoming traffic
    print("\n" + "="*50)
    print("Processing Incoming Traffic")
    print("="*50)
    
    incoming_traffic = [
        {"source_ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
        {"source_ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
        {"source_ip": "10.0.0.50", "port": 443, "protocol": "TCP"},
        {"source_ip": "192.168.1.10", "port": 80, "protocol": "TCP"},
        {"source_ip": "203.0.113.100", "port": 22, "protocol": "TCP"},
        {"source_ip": "203.0.113.100", "port": 23, "protocol": "TCP"},
    ]
    
    for i, packet in enumerate(incoming_traffic, 1):
        print(f"\n--- Packet {i} ---")
        print(f"Source: {packet['source_ip']} | Port: {packet['port']}")
        
        # Check if source IP is blocked
        if monitor.is_blocked(packet["source_ip"]):
            print("✗ BLOCKED: Source IP is on blocklist")
            monitor.log_event(SecurityEvent(
                "BLOCKED_TRAFFIC",
                packet["source_ip"],
                f"Traffic blocked from banned IP",
                "MEDIUM"
            ))
            continue
        
        # Check firewall rules
        action, rule_name = firewall.check_packet(packet)
        
        if action == RuleAction.ALLOW:
            print(f"✓ ALLOWED by rule: {rule_name}")
        else:
            print(f"✗ DENIED (default policy)")
            # Log suspicious denied traffic
            monitor.log_event(SecurityEvent(
                "DENIED_CONNECTION",
                packet["source_ip"],
                f"Denied connection attempt to port {packet['port']}",
                "LOW"
            ))
            
            # Check if IP should be blocked
            if monitor.is_blocked(packet["source_ip"]):
                print(f"⚠ IP {packet['source_ip']} auto-blocked after threshold reached")
    
    # Show final statistics
    print("\n" + "="*50)
    print("Security Summary")
    print("="*50)
    
    stats = monitor.get_statistics()
    print(f"\nTotal Packets Processed: {len(incoming_traffic)}")
    print(f"Security Events Logged: {stats['total_events']}")
    print(f"Unique Sources: {stats['unique_sources']}")
    print(f"Blocked IPs: {stats['blocked_ips']}")
    
    print("\nFirewall Rules Active:", len(firewall.list_rules()))
    
    if monitor.blocked_ips:
        print("\nBlocked IPs:")
        for ip in monitor.blocked_ips:
            print(f"  • {ip} ({monitor.ip_event_counts[ip]} events)")
    
    print("\n" + "="*50)
    print("Integrated example completed!")
    print("="*50)


if __name__ == "__main__":
    main()
