#!/usr/bin/env python3
"""
Security monitoring example for IRONWALL
"""
from ironwall.monitor import SecurityMonitor, SecurityEvent


def main():
    print("=== IRONWALL Security Monitor Example ===\n")
    
    # Create a security monitor
    monitor = SecurityMonitor()
    monitor.set_threat_threshold(3)
    print(f"Created security monitor with threat threshold: {monitor.threat_threshold}")
    
    print("\n" + "="*50)
    print("Simulating Security Events")
    print("="*50)
    
    # Simulate various security events
    events = [
        SecurityEvent("PORT_SCAN", "192.168.1.50", "Port scan detected on ports 22-100", "MEDIUM"),
        SecurityEvent("FAILED_LOGIN", "10.0.0.100", "Failed SSH login attempt", "LOW"),
        SecurityEvent("FAILED_LOGIN", "10.0.0.100", "Failed SSH login attempt", "LOW"),
        SecurityEvent("FAILED_LOGIN", "10.0.0.100", "Failed SSH login attempt", "MEDIUM"),
        SecurityEvent("SQL_INJECTION", "203.0.113.50", "SQL injection attempt detected", "HIGH"),
        SecurityEvent("DDoS_ATTEMPT", "192.168.1.50", "High traffic volume detected", "HIGH"),
        SecurityEvent("MALWARE", "192.168.1.50", "Malware signature detected", "CRITICAL"),
    ]
    
    print("\nLogging security events...")
    for event in events:
        monitor.log_event(event)
        blocked_status = " [AUTO-BLOCKED]" if monitor.is_blocked(event.source_ip) else ""
        print(f"\n✓ [{event.severity}] {event.event_type}")
        print(f"  Source: {event.source_ip}")
        print(f"  Description: {event.description}")
        print(f"  Time: {event.timestamp.strftime('%Y-%m-%d %H:%M:%S')}{blocked_status}")
    
    # Show statistics
    print("\n" + "="*50)
    print("Security Statistics")
    print("="*50)
    stats = monitor.get_statistics()
    print(f"\nTotal Events: {stats['total_events']}")
    print(f"Unique Sources: {stats['unique_sources']}")
    print(f"Blocked IPs: {stats['blocked_ips']}")
    
    # Show blocked IPs
    print("\n" + "="*50)
    print("Blocked IP Addresses")
    print("="*50)
    if monitor.blocked_ips:
        for ip in monitor.blocked_ips:
            count = monitor.ip_event_counts[ip]
            print(f"\n✗ {ip}")
            print(f"  Event count: {count}")
            print(f"  Status: BLOCKED (exceeded threshold of {monitor.threat_threshold})")
    else:
        print("\nNo IPs are currently blocked.")
    
    # Filter high severity events
    print("\n" + "="*50)
    print("High Severity Events")
    print("="*50)
    high_severity = monitor.get_events(severity="HIGH")
    print(f"\nFound {len(high_severity)} high severity events:")
    for event in high_severity:
        print(f"\n• {event.event_type} from {event.source_ip}")
        print(f"  {event.description}")
    
    # Example of unblocking an IP
    print("\n" + "="*50)
    print("Manual IP Management")
    print("="*50)
    test_ip = "192.168.1.50"
    if monitor.is_blocked(test_ip):
        print(f"\n{test_ip} is currently blocked")
        print(f"Unblocking {test_ip}...")
        monitor.unblock_ip(test_ip)
        print(f"✓ {test_ip} has been unblocked")
    
    print("\n" + "="*50)
    print("Example completed!")
    print("="*50)


if __name__ == "__main__":
    main()
