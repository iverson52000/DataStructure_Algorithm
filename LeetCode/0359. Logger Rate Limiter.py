"""
$359. Logger Rate Limiter
Design a logger system that receive stream of messages along with its timestamps, each message should 
be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed 
n the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.
"""

#hashmap

m = {}

if message not in m:
    m[message] = timestamp
    return True
if timestamp-m[message] >= 10:
    m[message] = timestamp
    return True
return False

