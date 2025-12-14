"""
Firewall implementation for IRONWALL
"""
from typing import List, Optional
from .rules import Rule, RuleAction


class Firewall:
    """Main firewall class for managing and applying rules"""
    
    def __init__(self):
        self.rules: List[Rule] = []
        self.default_action = RuleAction.DENY
    
    def add_rule(self, rule: Rule) -> None:
        """
        Add a rule to the firewall
        
        Args:
            rule: Rule object to add
        """
        self.rules.append(rule)
        # Sort rules by priority (higher priority first)
        self.rules.sort(key=lambda r: r.priority, reverse=True)
    
    def remove_rule(self, rule_name: str) -> bool:
        """
        Remove a rule from the firewall by name
        
        Args:
            rule_name: Name of the rule to remove
            
        Returns:
            True if rule was removed, False if not found
        """
        initial_count = len(self.rules)
        self.rules = [r for r in self.rules if r.name != rule_name]
        return len(self.rules) < initial_count
    
    def get_rule(self, rule_name: str) -> Optional[Rule]:
        """
        Get a rule by name
        
        Args:
            rule_name: Name of the rule to find
            
        Returns:
            Rule object if found, None otherwise
        """
        for rule in self.rules:
            if rule.name == rule_name:
                return rule
        return None
    
    def check_packet(self, packet: dict) -> tuple[RuleAction, Optional[str]]:
        """
        Check a packet against all rules
        
        Args:
            packet: Dictionary containing packet information
            
        Returns:
            Tuple of (action, rule_name) - action to take and name of matching rule
        """
        for rule in self.rules:
            if rule.matches(packet):
                return rule.action, rule.name
        return self.default_action, None
    
    def list_rules(self) -> List[Rule]:
        """
        Get all rules
        
        Returns:
            List of all rules
        """
        return self.rules.copy()
    
    def clear_rules(self) -> None:
        """Remove all rules"""
        self.rules.clear()
    
    def set_default_action(self, action: RuleAction) -> None:
        """
        Set the default action for packets that don't match any rule
        
        Args:
            action: Default action to set
        """
        self.default_action = action
