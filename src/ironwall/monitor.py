"""
Security monitoring component for IRONWALL
"""
from typing import List, Dict, Optional
from datetime import datetime
from collections import defaultdict


class SecurityEvent:
    """Represents a security event"""
    
    def __init__(self, event_type: str, source_ip: str, description: str, 
                 severity: str = "INFO"):
        self.event_type = event_type
        self.source_ip = source_ip
        self.description = description
        self.severity = severity
        self.timestamp = datetime.now()
    
    def __repr__(self) -> str:
        return (f"SecurityEvent(type='{self.event_type}', source='{self.source_ip}', "
                f"severity='{self.severity}', time='{self.timestamp}')")


class SecurityMonitor:
    """Monitor security events and detect threats"""
    
    def __init__(self):
        self.events: List[SecurityEvent] = []
        self.blocked_ips: set = set()
        self.threat_threshold = 5  # Number of events before flagging as threat
        self.ip_event_counts: Dict[str, int] = defaultdict(int)
    
    def log_event(self, event: SecurityEvent) -> None:
        """
        Log a security event
        
        Args:
            event: SecurityEvent to log
        """
        self.events.append(event)
        self.ip_event_counts[event.source_ip] += 1
        
        # Auto-block IPs that exceed threshold
        if self.ip_event_counts[event.source_ip] >= self.threat_threshold:
            self.block_ip(event.source_ip)
    
    def block_ip(self, ip_address: str) -> None:
        """
        Block an IP address
        
        Args:
            ip_address: IP address to block
        """
        self.blocked_ips.add(ip_address)
    
    def unblock_ip(self, ip_address: str) -> bool:
        """
        Unblock an IP address
        
        Args:
            ip_address: IP address to unblock
            
        Returns:
            True if IP was unblocked, False if it wasn't blocked
        """
        if ip_address in self.blocked_ips:
            self.blocked_ips.remove(ip_address)
            return True
        return False
    
    def is_blocked(self, ip_address: str) -> bool:
        """
        Check if an IP address is blocked
        
        Args:
            ip_address: IP address to check
            
        Returns:
            True if blocked, False otherwise
        """
        return ip_address in self.blocked_ips
    
    def get_events(self, source_ip: Optional[str] = None, 
                   severity: Optional[str] = None) -> List[SecurityEvent]:
        """
        Get security events, optionally filtered
        
        Args:
            source_ip: Filter by source IP (optional)
            severity: Filter by severity (optional)
            
        Returns:
            List of matching security events
        """
        events = self.events
        
        if source_ip:
            events = [e for e in events if e.source_ip == source_ip]
        
        if severity:
            events = [e for e in events if e.severity == severity]
        
        return events
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get monitoring statistics
        
        Returns:
            Dictionary with statistics
        """
        return {
            "total_events": len(self.events),
            "blocked_ips": len(self.blocked_ips),
            "unique_sources": len(self.ip_event_counts),
        }
    
    def clear_events(self) -> None:
        """Clear all logged events"""
        self.events.clear()
        self.ip_event_counts.clear()
    
    def set_threat_threshold(self, threshold: int) -> None:
        """
        Set the threat detection threshold
        
        Args:
            threshold: Number of events before flagging as threat
        """
        if threshold > 0:
            self.threat_threshold = threshold
