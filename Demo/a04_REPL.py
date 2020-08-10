In [19]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.

In [20]: a = {}

In [21]: help(a)
Help on dict object:

In [23]: len(a)
Out[23]: 0

In [24]: dir(a)
Out[24]:
['__class__',

In [26]: [d for d in dir(a) if '__' not in d]
Out[26]:
['clear',

In [27]: import inspect

In [28]: inspect.getfile(this)
Out[28]: 'D:\\Software\\Programs\\Python\\Python380-32\\lib\\this.py'

In [30]: import os

In [31]: clear = lambda: os.system('cls')

In [33]: clear()

In [37]: a = 2

In [38]: b = 3

In [39]: a ^= b

In [40]: b ^= a

In [41]: a ^= b

In [42]: a
Out[42]: 3

In [43]: b
Out[43]: 2

In [45]: a = [[1, 2, 3], [4, 5, 6]]

In [46]: [[r[c] for r in a] for c in range(3)]
Out[46]: [[1, 4], [2, 5], [3, 6]]

In [49]: b = [1, 2, 3]

In [50]: c = [4, 5, 6]

In [51]: list(x * y for x, y in zip(b, c))
Out[51]: [4, 10, 18]

In [53]: import re

In [54]: s = 'if 2+2 is 4 then 1+2+3+4 is 10'

In [55]: p = re.compile(r'(\d+)\+(\d+)', re.IGNORECASE)

In [56]: r = p.sub(lambda m: str(int(m.group(1)) + int(m.group(2))), s)

In [57]: r
Out[57]: 'if 4 is 4 then 3+7 is 10'

# numpy: create array
In [2]: import numpy as np

In [43]: a = np.ones([5, 5])

In [44]: a
Out[44]:
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

In [45]: b = np.zeros([3, 3])

In [46]: b
Out[46]:
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])

In [47]: b[1, 1] = 9

In [48]: b
Out[48]:
array([[0., 0., 0.],
       [0., 9., 0.],
       [0., 0., 0.]])

In [49]: a[1:-1, 1:-1] = b

In [51]: a
Out[51]:
array([[1., 1., 1., 1., 1.],
       [1., 0., 0., 0., 1.],
       [1., 0., 9., 0., 1.],
       [1., 0., 0., 0., 1.],
       [1., 1., 1., 1., 1.]])

# numpy: indexing with boolean array
In [2]: import numpy as np

In [3]: a = np.arange(15)

In [4]: a
Out[4]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

In [6]: a = np.arange(15).reshape(3, 5)
In [7]: a
Out[7]:
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

In [14]: b = a > 4

In [15]: b
Out[15]:
array([[False, False, False, False, False],
       [ True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True]])

In [16]: a[b]
Out[16]: array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

In [19]: a[b] = 99

In [20]: a
Out[20]:
array([[ 0,  1,  2,  3,  4],
       [99, 99, 99, 99, 99],
       [99, 99, 99, 99, 99]])

