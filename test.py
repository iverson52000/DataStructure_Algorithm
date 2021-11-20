import collections
import threading
import time
import queue
from collections import *
from typing import List
import random


# APIs
# list_folder("/home/airtable") returns ["Backups", ".bashrc", "Photos", "profile.jpeg", ...]
# is_folder("/home/airtable/Backups") returns true
# is_folder("/home/airtable/.bashrc") returns false

def list_folder():
    pass


def is_folder():
    pass


def getContent():
    pass


def find_dupes(root_path: str) -> List[List[str]]:
    m = collections.defaultdict(list)
    q = collections.deque([root_path])

    while q:
        rootPath = q.popleft()
        paths = [rootPath+'/'+item for item in list_folder(rootPath)]

        for path in paths:
            if not is_folder(path):
                fileName = path.split('/')[-1]
                # get content?
                content = getContent(fileName)
                m[content].append(path)

            nextPath = rootPath+'/'+path
            q.append(nextPath)

    return [val for val in m.values() if len(val) > 1]


def find_dupes(root_path: str) -> List[List[str]]:
    m = collections.defaultdict(list)

    def dfs(rootPath: str):
        if not is_folder(rootPath):
            fileName = rootPath.split('/')[-1]
            # get content?
            content = getContent(fileName)
            m[content].append(rootPath)

        paths = [rootPath+'/'+item for item in list_folder(rootPath)]

        for path in paths:
            nextPath = rootPath+'/'+path
            dfs(nextPath)

    dfs(root_path)

    return [val for val in m.values() if len(val) > 1]


# 20211117
