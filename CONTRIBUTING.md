# Contributing to IRONWALL

Thank you for your interest in contributing to IRONWALL! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/IRONWALL.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit and push
7. Create a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/secure-s/IRONWALL.git
cd IRONWALL

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt
```

## Coding Standards

### Python Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Keep functions focused and small
- Maximum line length: 88 characters (Black default)

### Documentation

- Add docstrings to all public classes and functions
- Include type hints where appropriate
- Update README.md for new features
- Comment complex logic

### Example:

```python
def check_packet(self, packet: dict) -> tuple[RuleAction, Optional[str]]:
    """
    Check a packet against all rules
    
    Args:
        packet: Dictionary containing packet information
        
    Returns:
        Tuple of (action, rule_name) - action to take and name of matching rule
    """
    # Implementation here
```

## Testing

### Writing Tests

- Write tests for all new features
- Maintain existing test coverage
- Test edge cases and error conditions
- Use descriptive test names

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=ironwall tests/

# Run specific test file
pytest tests/test_firewall.py -v
```

### Test Structure

```python
def test_feature_description():
    """Test that feature behaves correctly under specific conditions"""
    # Setup
    firewall = Firewall()
    rule = Rule(name="test", action=RuleAction.ALLOW)
    
    # Execute
    firewall.add_rule(rule)
    
    # Assert
    assert len(firewall.list_rules()) == 1
```

## Pull Request Process

1. **Create a Branch**
   - Use descriptive branch names: `feature/add-time-based-rules`, `fix/rule-matching-bug`

2. **Make Changes**
   - Keep changes focused and atomic
   - Write clear commit messages
   - Follow coding standards

3. **Write Tests**
   - Add tests for new functionality
   - Ensure all tests pass
   - Maintain or improve coverage

4. **Update Documentation**
   - Update README.md if needed
   - Add docstrings to new code
   - Update ASSIGNMENT.md for new features

5. **Submit Pull Request**
   - Provide clear description
   - Reference any related issues
   - List changes made

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
```

## Feature Requests

When proposing a new feature:

1. Check existing issues first
2. Describe the feature clearly
3. Explain the use case
4. Consider security implications
5. Discuss implementation approach

## Bug Reports

When reporting a bug:

1. Check if it's already reported
2. Provide clear description
3. Include steps to reproduce
4. Share relevant code snippets
5. Note your environment (Python version, OS)

### Bug Report Template

```markdown
**Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce the behavior:
1. Create firewall with...
2. Add rule...
3. Check packet...
4. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- Python version:
- IRONWALL version:
- Operating System:

**Additional Context**
Any other relevant information
```

## Commit Message Guidelines

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor to..." not "Moves cursor to..."
- First line: brief summary (50 chars or less)
- Blank line, then detailed description if needed

### Examples:

```
Add time-based rule filtering

Implement support for rules that only apply during specific time ranges.
This allows for business-hours policies and scheduled access control.

Add IP range support using CIDR notation

Allow rules to match entire IP ranges instead of single IPs.
Supports both IPv4 and IPv6 CIDR notation.
```

## Areas for Contribution

### Good First Issues

- Add more example scripts
- Improve error messages
- Add input validation
- Enhance documentation
- Write additional tests

### Feature Enhancements

- Time-based rules
- IP range support (CIDR)
- Rate limiting
- Connection tracking
- Geolocation filtering
- Web dashboard
- Configuration file support

### Performance Improvements

- Rule matching optimization
- Indexing for large rule sets
- Memory usage optimization
- Parallel packet processing

### Documentation

- Tutorial guides
- Architecture documentation
- API documentation
- Video tutorials
- Blog posts

## Questions?

If you have questions:
- Open an issue with the "question" label
- Check existing documentation
- Review example code

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Thank You!

Your contributions help make IRONWALL better for everyone learning network security!
