# IRONWALL

A Python-based security monitoring and firewall management system for learning network security concepts.

## Overview

IRONWALL is an educational security framework that demonstrates core concepts of:
- Firewall rule management and packet filtering
- Security event monitoring and threat detection
- Automatic IP blocking based on threat thresholds
- Rule-based access control with priority handling

## Features

### Firewall
- ✅ Rule-based packet filtering
- ✅ Priority-based rule processing
- ✅ Support for multiple criteria (IP, port, protocol)
- ✅ Configurable default policy (ALLOW/DENY)
- ✅ Dynamic rule management (add/remove/list)

### Security Monitor
- ✅ Event logging and tracking
- ✅ Automatic threat detection
- ✅ IP-based blocking with thresholds
- ✅ Event filtering by source and severity
- ✅ Real-time security statistics

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/secure-s/IRONWALL.git
cd IRONWALL

# Install the package
pip install -e .

# Install development dependencies (optional)
pip install -r requirements.txt
```

## Quick Start

### Basic Firewall Usage

```python
from ironwall import Firewall, Rule, RuleAction

# Create a firewall
firewall = Firewall()

# Add a rule to allow HTTP traffic
firewall.add_rule(Rule(
    name="allow_http",
    action=RuleAction.ALLOW,
    port=80,
    protocol="TCP"
))

# Check a packet
packet = {"port": 80, "protocol": "TCP", "source_ip": "192.168.1.1"}
action, rule_name = firewall.check_packet(packet)
print(f"Action: {action}, Matched Rule: {rule_name}")
```

### Security Monitoring

```python
from ironwall.monitor import SecurityMonitor, SecurityEvent

# Create a monitor
monitor = SecurityMonitor()
monitor.set_threat_threshold(3)

# Log a security event
event = SecurityEvent(
    event_type="FAILED_LOGIN",
    source_ip="10.0.0.100",
    description="Failed SSH login attempt",
    severity="MEDIUM"
)
monitor.log_event(event)

# Check if an IP is blocked
if monitor.is_blocked("10.0.0.100"):
    print("IP is blocked!")
```

## Examples

The `examples/` directory contains comprehensive examples:

1. **firewall_example.py** - Demonstrates firewall rule management and packet filtering
2. **monitor_example.py** - Shows security event monitoring and threat detection
3. **integrated_example.py** - Combines both firewall and monitor in a real scenario

Run examples:

```bash
# Run from the repository root
python examples/firewall_example.py
python examples/monitor_example.py
python examples/integrated_example.py
```

## Running Tests

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_firewall.py

# Run with verbose output
pytest -v tests/
```

## Architecture

### Core Components

1. **Rules Module** (`ironwall/rules.py`)
   - `Rule`: Defines firewall rules with matching criteria
   - `RuleAction`: Enum for rule actions (ALLOW, DENY, LOG)

2. **Firewall Module** (`ironwall/firewall.py`)
   - `Firewall`: Main firewall class for rule management and packet filtering
   - Priority-based rule processing
   - Configurable default policy

3. **Monitor Module** (`ironwall/monitor.py`)
   - `SecurityEvent`: Represents a security event
   - `SecurityMonitor`: Tracks events, detects threats, manages blocked IPs
   - Automatic blocking based on configurable thresholds

## API Reference

### Firewall Class

```python
firewall = Firewall()

# Add a rule
firewall.add_rule(rule)

# Remove a rule by name
firewall.remove_rule("rule_name")

# Check a packet against rules
action, rule_name = firewall.check_packet(packet)

# List all rules
rules = firewall.list_rules()

# Set default action
firewall.set_default_action(RuleAction.ALLOW)
```

### SecurityMonitor Class

```python
monitor = SecurityMonitor()

# Log an event
monitor.log_event(event)

# Block/unblock IPs
monitor.block_ip("192.168.1.1")
monitor.unblock_ip("192.168.1.1")

# Check if IP is blocked
is_blocked = monitor.is_blocked("192.168.1.1")

# Get events (with optional filters)
events = monitor.get_events(source_ip="192.168.1.1", severity="HIGH")

# Get statistics
stats = monitor.get_statistics()
```

## Assignment Tasks

This project can be used for various security-related assignments:

1. **Basic Implementation** - Understand the existing codebase
2. **Rule Enhancement** - Add new rule types (e.g., time-based rules)
3. **Advanced Filtering** - Implement stateful packet inspection
4. **Logging System** - Add persistent logging to files or databases
5. **Alert System** - Implement notifications for security events
6. **Performance** - Optimize rule matching for large rule sets
7. **Integration** - Connect to actual network interfaces
8. **Visualization** - Create dashboards for monitoring

## Contributing

Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run the test suite
5. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Educational Use

IRONWALL is designed for learning purposes to understand:
- Network security fundamentals
- Firewall architecture and implementation
- Security event monitoring
- Threat detection and response
- Python programming best practices

**Note**: This is an educational tool and should not be used as a production firewall system.

## Support

For questions or issues, please open an issue on the GitHub repository.