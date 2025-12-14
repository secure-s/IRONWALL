"""
Tests for IRONWALL security monitor module
"""
import pytest
from ironwall.monitor import SecurityMonitor, SecurityEvent


def test_security_event_creation():
    """Test creating a security event"""
    event = SecurityEvent(
        event_type="INTRUSION_ATTEMPT",
        source_ip="192.168.1.100",
        description="Multiple failed login attempts",
        severity="HIGH"
    )
    
    assert event.event_type == "INTRUSION_ATTEMPT"
    assert event.source_ip == "192.168.1.100"
    assert event.severity == "HIGH"
    assert event.timestamp is not None


def test_monitor_creation():
    """Test creating a security monitor"""
    monitor = SecurityMonitor()
    assert len(monitor.events) == 0
    assert len(monitor.blocked_ips) == 0
    assert monitor.threat_threshold == 5


def test_log_event():
    """Test logging a security event"""
    monitor = SecurityMonitor()
    event = SecurityEvent(
        event_type="PORT_SCAN",
        source_ip="10.0.0.1",
        description="Port scanning detected"
    )
    
    monitor.log_event(event)
    assert len(monitor.events) == 1
    assert monitor.ip_event_counts["10.0.0.1"] == 1


def test_auto_block_on_threshold():
    """Test automatic IP blocking when threshold is reached"""
    monitor = SecurityMonitor()
    monitor.set_threat_threshold(3)
    
    # Log 3 events from same IP
    for i in range(3):
        event = SecurityEvent(
            event_type="SUSPICIOUS_ACTIVITY",
            source_ip="192.168.1.50",
            description=f"Event {i}"
        )
        monitor.log_event(event)
    
    # IP should be auto-blocked
    assert monitor.is_blocked("192.168.1.50") is True


def test_block_unblock_ip():
    """Test manually blocking and unblocking IPs"""
    monitor = SecurityMonitor()
    
    monitor.block_ip("10.0.0.1")
    assert monitor.is_blocked("10.0.0.1") is True
    
    result = monitor.unblock_ip("10.0.0.1")
    assert result is True
    assert monitor.is_blocked("10.0.0.1") is False
    
    # Unblock non-blocked IP
    result = monitor.unblock_ip("10.0.0.2")
    assert result is False


def test_get_events_no_filter():
    """Test getting all events without filter"""
    monitor = SecurityMonitor()
    
    event1 = SecurityEvent("EVENT1", "192.168.1.1", "Test 1", "LOW")
    event2 = SecurityEvent("EVENT2", "192.168.1.2", "Test 2", "HIGH")
    
    monitor.log_event(event1)
    monitor.log_event(event2)
    
    events = monitor.get_events()
    assert len(events) == 2


def test_get_events_filter_by_ip():
    """Test filtering events by source IP"""
    monitor = SecurityMonitor()
    
    event1 = SecurityEvent("EVENT1", "192.168.1.1", "Test 1")
    event2 = SecurityEvent("EVENT2", "192.168.1.2", "Test 2")
    event3 = SecurityEvent("EVENT3", "192.168.1.1", "Test 3")
    
    monitor.log_event(event1)
    monitor.log_event(event2)
    monitor.log_event(event3)
    
    events = monitor.get_events(source_ip="192.168.1.1")
    assert len(events) == 2


def test_get_events_filter_by_severity():
    """Test filtering events by severity"""
    monitor = SecurityMonitor()
    
    event1 = SecurityEvent("EVENT1", "192.168.1.1", "Test 1", "LOW")
    event2 = SecurityEvent("EVENT2", "192.168.1.2", "Test 2", "HIGH")
    event3 = SecurityEvent("EVENT3", "192.168.1.3", "Test 3", "HIGH")
    
    monitor.log_event(event1)
    monitor.log_event(event2)
    monitor.log_event(event3)
    
    events = monitor.get_events(severity="HIGH")
    assert len(events) == 2


def test_get_statistics():
    """Test getting monitor statistics"""
    monitor = SecurityMonitor()
    
    monitor.log_event(SecurityEvent("EVENT1", "192.168.1.1", "Test"))
    monitor.log_event(SecurityEvent("EVENT2", "192.168.1.2", "Test"))
    monitor.log_event(SecurityEvent("EVENT3", "192.168.1.1", "Test"))
    monitor.block_ip("10.0.0.1")
    
    stats = monitor.get_statistics()
    assert stats["total_events"] == 3
    assert stats["blocked_ips"] == 1
    assert stats["unique_sources"] == 2


def test_clear_events():
    """Test clearing all events"""
    monitor = SecurityMonitor()
    
    monitor.log_event(SecurityEvent("EVENT1", "192.168.1.1", "Test"))
    monitor.log_event(SecurityEvent("EVENT2", "192.168.1.2", "Test"))
    
    assert len(monitor.events) == 2
    
    monitor.clear_events()
    assert len(monitor.events) == 0
    assert len(monitor.ip_event_counts) == 0
