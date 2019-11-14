"""
551. Student Attendance Record I
You are given a string representing an attendance record for a student. The record only contains the following three characters:
1.	'A' : Absent.
2.	'L' : Late.
3.	'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.
"""

#traverse

class Solution:
    def checkRecord(self, s: str) -> bool:
        if not s: return False
        a = 0
        for i in range(len(s)): 
            if s[i] == 'A': 
                a+=1
                if a==2: return False 
            elif i < len(s)-1 and s[i:i+3] == "LLL": return False 
        return True

#pythonic

class Solution:
    def checkRecord(self, s: str) -> bool:
        if not s: return False
        return s.count('A') < 2 and s.count('LLL') == 0

