"""
Tests for IRONWALL rules module
"""
import pytest
from ironwall.rules import Rule, RuleAction


def test_rule_creation():
    """Test creating a basic rule"""
    rule = Rule(
        name="test_rule",
        action=RuleAction.ALLOW,
        source_ip="192.168.1.1",
        port=80
    )
    assert rule.name == "test_rule"
    assert rule.action == RuleAction.ALLOW
    assert rule.source_ip == "192.168.1.1"
    assert rule.port == 80


def test_rule_matches_all_criteria():
    """Test rule matching with all criteria"""
    rule = Rule(
        name="strict_rule",
        action=RuleAction.DENY,
        source_ip="10.0.0.1",
        dest_ip="10.0.0.2",
        port=443,
        protocol="TCP"
    )
    
    packet = {
        "source_ip": "10.0.0.1",
        "dest_ip": "10.0.0.2",
        "port": 443,
        "protocol": "TCP"
    }
    
    assert rule.matches(packet) is True


def test_rule_no_match():
    """Test rule not matching"""
    rule = Rule(
        name="test_rule",
        action=RuleAction.DENY,
        source_ip="10.0.0.1",
        port=80
    )
    
    packet = {
        "source_ip": "10.0.0.2",  # Different IP
        "port": 80
    }
    
    assert rule.matches(packet) is False


def test_rule_partial_match():
    """Test rule with partial criteria"""
    rule = Rule(
        name="partial_rule",
        action=RuleAction.ALLOW,
        port=22
    )
    
    # Should match any packet with port 22
    packet1 = {
        "source_ip": "192.168.1.1",
        "port": 22
    }
    packet2 = {
        "source_ip": "10.0.0.1",
        "port": 22,
        "protocol": "TCP"
    }
    
    assert rule.matches(packet1) is True
    assert rule.matches(packet2) is True


def test_rule_actions():
    """Test different rule actions"""
    assert RuleAction.ALLOW.value == "allow"
    assert RuleAction.DENY.value == "deny"
    assert RuleAction.LOG.value == "log"
