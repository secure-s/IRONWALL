"""
Rule definitions for IRONWALL firewall
"""
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class RuleAction(Enum):
    """Actions that can be taken on network traffic"""
    ALLOW = "allow"
    DENY = "deny"
    LOG = "log"


@dataclass
class Rule:
    """Represents a firewall rule"""
    name: str
    action: RuleAction
    source_ip: Optional[str] = None
    dest_ip: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    priority: int = 0
    
    def matches(self, packet: dict) -> bool:
        """
        Check if this rule matches a given packet
        
        Args:
            packet: Dictionary containing packet information
            
        Returns:
            True if the rule matches, False otherwise
        """
        if self.source_ip and packet.get("source_ip") != self.source_ip:
            return False
        if self.dest_ip and packet.get("dest_ip") != self.dest_ip:
            return False
        if self.port and packet.get("port") != self.port:
            return False
        if self.protocol and packet.get("protocol") != self.protocol:
            return False
        return True
    
    def __repr__(self) -> str:
        return (f"Rule(name='{self.name}', action={self.action.value}, "
                f"source_ip={self.source_ip}, dest_ip={self.dest_ip}, "
                f"port={self.port}, protocol={self.protocol}, priority={self.priority})")
