import collections
import threading
import time
import queue
from collections import *
from typing import List
import random
from hashlib import md5

# input = "/home/airtable"
# output = [
#     [".bashrc", "Backups/2017_bashrc"],
#     ["Photos/Vacation/DSC1234.JPG", "profile.jpeg", ".trash/lej2dp28/87msnlgyr"],
# ]

# APIs
# list_folder("/home/airtable") returns ["Backups", ".bashrc", "Photos", "profile.jpeg", ...]
# is_folder("/home/airtable/Backups") returns true
# is_folder("/home/airtable/.bashrc") returns false


def list_folder(path: str) -> List[str]:
    """Return file or folder name only"""
    pass


def is_folder(path: str) -> bool:
    """Return true if is folder"""
    pass


def getContent(path: str) -> str:
    try:
        with open(path) as file:
            lines = file.readlines()
            return ''.join(lines)
    except Exception as err:
        print('Error!'+err)
        # raise err


# bfs
def find_dupes(root_path: str) -> List[List[str]]:
    if not root_path:
        return []

    m = collections.defaultdict(list)
    q = collections.deque([root_path])

    while q:
        curPath = q.popleft()
        paths = [curPath+'/'+name for name in list_folder(curPath)]

        for path in paths:
            if not is_folder(path):
                # subPath = path.split(root_path)[-1]
                # get content?
                # hashlib.md5(content.encode())
                content = getContent(path)
                m[content].append(path)
            else:
                q.append(path)

    return [val for val in m.values() if len(val) > 1]


# dfs
def find_dupes(root_path: str) -> List[List[str]]:
    if not root_path:
        return []

    m = collections.defaultdict(list)

    def dfs(curPath: str):
        if not curPath:
            return

        if not is_folder(curPath):
            # subPath = curPath.split(root_path)[-1]
            # get content?
            content = getContent(curPath)
            m[content].append(curPath)
            return

        paths = [curPath+'/'+name for name in list_folder(curPath)]

        for path in paths:
            dfs(path)

    dfs(root_path)

    return [val for val in m.values() if len(val) > 1]


arr = [1, 2, 3, 'a', 7]

for item in arr:
    try:
        if isinstance(item, str):
            raise Exception("string!")
        else:
            print(item)
    except Exception as err:
        print(err)

print(md5(b"testing!!!"))

root = "/home/airtable"
path1 = "/home/airtable/Backups/2017_bashrc"
print(path1.split(root+"/")[-1])
