"""
Tests for IRONWALL firewall module
"""
import pytest
from ironwall.firewall import Firewall
from ironwall.rules import Rule, RuleAction


def test_firewall_creation():
    """Test creating a firewall"""
    fw = Firewall()
    assert fw.default_action == RuleAction.DENY
    assert len(fw.list_rules()) == 0


def test_add_rule():
    """Test adding a rule to firewall"""
    fw = Firewall()
    rule = Rule(name="allow_http", action=RuleAction.ALLOW, port=80)
    
    fw.add_rule(rule)
    assert len(fw.list_rules()) == 1
    assert fw.get_rule("allow_http") == rule


def test_remove_rule():
    """Test removing a rule"""
    fw = Firewall()
    rule = Rule(name="test_rule", action=RuleAction.DENY)
    
    fw.add_rule(rule)
    assert len(fw.list_rules()) == 1
    
    result = fw.remove_rule("test_rule")
    assert result is True
    assert len(fw.list_rules()) == 0
    
    # Try removing non-existent rule
    result = fw.remove_rule("non_existent")
    assert result is False


def test_check_packet_with_matching_rule():
    """Test checking a packet that matches a rule"""
    fw = Firewall()
    rule = Rule(
        name="allow_ssh",
        action=RuleAction.ALLOW,
        port=22,
        protocol="TCP"
    )
    fw.add_rule(rule)
    
    packet = {
        "port": 22,
        "protocol": "TCP",
        "source_ip": "192.168.1.1"
    }
    
    action, rule_name = fw.check_packet(packet)
    assert action == RuleAction.ALLOW
    assert rule_name == "allow_ssh"


def test_check_packet_default_action():
    """Test packet that doesn't match any rule uses default action"""
    fw = Firewall()
    rule = Rule(name="deny_80", action=RuleAction.DENY, port=80)
    fw.add_rule(rule)
    
    packet = {"port": 443}  # Doesn't match port 80
    
    action, rule_name = fw.check_packet(packet)
    assert action == RuleAction.DENY  # Default action
    assert rule_name is None


def test_rule_priority():
    """Test that rules are processed by priority"""
    fw = Firewall()
    
    # Lower priority rule
    rule1 = Rule(
        name="low_priority",
        action=RuleAction.DENY,
        port=80,
        priority=1
    )
    
    # Higher priority rule
    rule2 = Rule(
        name="high_priority",
        action=RuleAction.ALLOW,
        port=80,
        priority=10
    )
    
    fw.add_rule(rule1)
    fw.add_rule(rule2)
    
    packet = {"port": 80}
    action, rule_name = fw.check_packet(packet)
    
    # Should match high priority rule first
    assert action == RuleAction.ALLOW
    assert rule_name == "high_priority"


def test_set_default_action():
    """Test changing default action"""
    fw = Firewall()
    fw.set_default_action(RuleAction.ALLOW)
    
    packet = {"port": 9999}  # Won't match any rules
    action, rule_name = fw.check_packet(packet)
    
    assert action == RuleAction.ALLOW
    assert rule_name is None


def test_clear_rules():
    """Test clearing all rules"""
    fw = Firewall()
    fw.add_rule(Rule(name="rule1", action=RuleAction.ALLOW))
    fw.add_rule(Rule(name="rule2", action=RuleAction.DENY))
    
    assert len(fw.list_rules()) == 2
    
    fw.clear_rules()
    assert len(fw.list_rules()) == 0
