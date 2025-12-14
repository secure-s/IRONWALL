# IRONWALL Assignment Guide

## Assignment Overview

This assignment involves working with IRONWALL, an educational security monitoring and firewall management system. The project demonstrates core network security concepts through a Python implementation.

## Getting Started

### 1. Installation

```bash
# Navigate to the project directory
cd IRONWALL

# Install the package in development mode
pip install -e .

# Install testing dependencies
pip install -r requirements.txt
```

### 2. Understanding the Codebase

The project is organized as follows:

```
IRONWALL/
├── src/ironwall/          # Main source code
│   ├── __init__.py        # Package initialization
│   ├── rules.py           # Rule definitions
│   ├── firewall.py        # Firewall implementation
│   └── monitor.py         # Security monitoring
├── tests/                 # Unit tests
│   ├── test_rules.py
│   ├── test_firewall.py
│   └── test_monitor.py
├── examples/              # Usage examples
│   ├── firewall_example.py
│   ├── monitor_example.py
│   └── integrated_example.py
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

### 3. Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest -v tests/

# Run specific test file
pytest tests/test_firewall.py
```

### 4. Running Examples

```bash
# Firewall example
python examples/firewall_example.py

# Security monitoring example
python examples/monitor_example.py

# Integrated example
python examples/integrated_example.py
```

## Assignment Tasks

### Basic Tasks

1. **Explore the Code**
   - Read through all modules in `src/ironwall/`
   - Understand how rules are defined and matched
   - Study the firewall's rule processing logic
   - Examine the security monitor's event handling

2. **Run Tests**
   - Execute all test suites
   - Understand what each test validates
   - Ensure all tests pass

3. **Try Examples**
   - Run all example scripts
   - Modify examples to test different scenarios
   - Create your own packet filtering scenarios

### Intermediate Tasks

4. **Add New Rule Types**
   - Implement time-based rules (e.g., allow only during business hours)
   - Add support for IP ranges (CIDR notation)
   - Create rules that log without blocking

5. **Enhance Security Monitor**
   - Add event severity levels
   - Implement event persistence (save to file)
   - Create alert notifications for critical events

6. **Improve Testing**
   - Add edge case tests
   - Test with invalid inputs
   - Add performance tests for large rule sets

### Advanced Tasks

7. **Performance Optimization**
   - Profile rule matching performance
   - Optimize for large numbers of rules
   - Implement rule indexing

8. **Add New Features**
   - Stateful packet inspection
   - Connection tracking
   - Rate limiting per IP
   - Geolocation-based filtering

9. **Create Dashboard**
   - Web-based monitoring interface
   - Real-time event visualization
   - Rule management UI

10. **Integration**
    - Connect to actual network interfaces
    - Parse real packet data
    - Implement packet capture

## Evaluation Criteria

Your work will be evaluated on:

1. **Understanding** - Demonstrate comprehension of security concepts
2. **Code Quality** - Write clean, maintainable, documented code
3. **Testing** - Comprehensive test coverage for new features
4. **Security** - Consider security implications of changes
5. **Documentation** - Clear documentation of new features

## Resources

- **Python Documentation**: https://docs.python.org/3/
- **Network Security Basics**: Research firewall concepts, packet filtering
- **pytest Documentation**: https://docs.pytest.org/

## Tips

1. Start with the basic tasks before moving to advanced ones
2. Write tests for any new functionality you add
3. Keep security in mind - validate inputs, handle errors
4. Document your code with clear docstrings
5. Ask questions if you're stuck!

## Common Commands

```bash
# Install package
pip install -e .

# Run all tests
pytest tests/

# Run tests with coverage
pytest --cov=ironwall tests/

# Run specific test
pytest tests/test_firewall.py::test_add_rule -v

# Format code (if using black)
black src/ tests/

# Type checking (if using mypy)
mypy src/

# Run example
python examples/firewall_example.py
```

## Troubleshooting

### Import Errors
If you get import errors, make sure you've installed the package:
```bash
pip install -e .
```

### Test Failures
If tests fail:
1. Check Python version (requires 3.7+)
2. Ensure all dependencies are installed
3. Run tests with `-v` flag for more details

### Example Not Working
Make sure you're in the correct directory and have installed the package.

## Submission Guidelines

When submitting your assignment:

1. Include all modified files
2. Add new test files for your features
3. Update README.md with new features
4. Include a summary of changes
5. Ensure all tests pass
6. Document any new dependencies

Good luck with your assignment!
