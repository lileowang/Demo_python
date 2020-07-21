"""
Description:
- Loop with zip for two or more lists
"""

names = ['a', 'b', 'c']
groups = ['x', 'y', 'z']
for name, group in zip(names, groups):
    print(f'{name} in {group}')
