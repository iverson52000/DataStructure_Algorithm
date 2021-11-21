import collections
import threading
import time
import queue
from collections import *
from typing import List
import random

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
    with open(path) as file:
        lines = file.readlines()

        return ''.join(lines)


print(getContent("test.js"))


# bfs
def find_dupes(root_path: str) -> List[List[str]]:
    if not root_path:
        return []

    m = collections.defaultdict(list)
    q = collections.deque([root_path])

    while q:
        rootPath = q.popleft()
        paths = [rootPath+'/'+name for name in list_folder(rootPath)]

        for path in paths:
            if not is_folder(path):
                # fileName = path.split('/')[-1]
                # get content?
                # hashlib.md5(content.encode())
                content = getContent(path)
                m[content].append(path)

            nextPath = rootPath+'/'+path
            q.append(nextPath)

    return [val for val in m.values() if len(val) > 1]


# dfs
def find_dupes(root_path: str) -> List[List[str]]:
    if not root_path:
        return []

    m = collections.defaultdict(list)

    def dfs(rootPath: str):
        if not rootPath:
            return

        if not is_folder(rootPath):
            # fileName = rootPath.split('/')[-1]
            # get content?
            content = getContent(rootPath)
            m[content].append(rootPath)
            return

        paths = [rootPath+'/'+name for name in list_folder(rootPath)]

        for path in paths:
            nextPath = rootPath+'/'+path
            dfs(nextPath)

    dfs(root_path)

    return [val for val in m.values() if len(val) > 1]


# 20211117
