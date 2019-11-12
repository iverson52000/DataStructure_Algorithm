"""
981. Time Based Key-Value Store
Create a timebased key-value store class TimeMap, that supports two operations.
1. set(string key, string value, int timestamp)
•	Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)
•	Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
•	If there are multiple such values, it returns the one with the largest timestamp_prev.
•	If there are no values, it returns the empty string ("").
"""

#two hashmap+binary search

class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''


