"""
Description:
- Unpack tuple with *_ for the rest not cared values
"""

a, b, *_ = (1, 2, 3, 4, 5)
print(a, b)
