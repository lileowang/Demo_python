"""
Description:
- Switch statement is not available in Python
- But it can implemented with dictionary
"""

def switch(idx):
    def one():
        return 'one'

    def two():
        return 'two'

    def three():
        return 'three'

    funcs = [
        one,
        two,
        three,
    ]

    i = [x for x in range(1, 4)]

    switcher = dict(zip(i, funcs))
    # print(switcher)

    func = switcher.get(idx, lambda: 'invalid')
    return func()

print(switch(2))
