"""
Author:     Li Leo Wang
Date:       2020-08-22
Description:
- Display directory tree of current folder

References:
https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python

"""

import sys
from pathlib import Path
from itertools import islice
# import pdb

space = '  '
branch = '|  '
mid = '|--'
last = '|__'


def tree(folder: Path,
         dir_only: bool = False,
         depth: int = -1,
         max_len: int = 1_000):
    """
    folder: given directory
    dir_only: True = only display subfolders
    depth: tree levels to be displayed
              False = display both files and subfolders
    max_len: limit the items to be displayed
    """

    folder = Path(folder)  # cast string to Path
    files = 0
    dirs = 0

    def inner(folder: Path, prefix: str = '', depth: int = -1):
        nonlocal files, dirs

        # debug only
        # pdb.set_trace()

        if not depth:
            return  # 0, reach required tree depth

        if dir_only:
            # only pick the directories
            contents = [d for d in folder.iterdir() if d.is_dir()]
        else:
            # list of all the files and subfolders
            contents = list(folder.iterdir())
        # debug only
        # print(contents)

        # collections of tree node markers
        markers = [mid] * (len(contents) - 1) + [last]
        # print(markers)

        # loop thru each node
        for marker, path in zip(markers, contents):
            if path.is_dir():
                # enclose folder name with square brackets []
                yield prefix + marker + '[' + path.name + ']'
                dirs += 1
                extension = branch if marker == mid else space
                yield from inner(path,
                                 prefix=prefix + extension,
                                 depth=depth - 1)
            elif not dir_only:
                yield prefix + marker + path.name
                files += 1

    # end: inner()

    print(folder.name)
    iterator = inner(folder, depth=depth)
    for line in islice(iterator, max_len):
        print(line)
    if next(iterator, None):
        # iterator is not None, not exhausted
        print(f'... max_len: {max_len}, reached')
    print(f'\n{dirs} subfolders, {files} files')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Args: [dir_only] [depth] [max_len]')
        print('example: 0 -1 -1')
        print('dir_only: 0 = files and subfolder, 1 = subfolder only')
        print('depth: -1 = full depth, positive number n = n levels')
        print(
            'max_len: -1 = default (1_000 items), positive number n = max n items'
        )
    else:
        dir_only = False if int(sys.argv[1]) == 0 else True
        depth = int(sys.argv[2])
        max_len = 1_000 if int(sys.argv[3]) < 0 else int(sys.argv[3])
        tree(Path.cwd(), dir_only, depth, max_len)
