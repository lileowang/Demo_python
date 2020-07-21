"""
Description:
- Context manager for reading file
"""

with open('main.py', 'r') as f:
    contents = f.read()
    print(contents)
