"""
Given two strings s and t, determine if they are both one edit distance apart.
Note: 
There are 3 possiblities to satisify one edit distance apart:
1.	Insert a character into s to get t
2.	Delete a character from s to get t
3.	Replace a character of s to get t
"""

#DS, algo: traverse. 3 cases

if len(s) < len(t): s, t = t, s
diff = len(s)-len(t)
if diff >= 2: return False
elif diff == 1:
	for i in range(len(t)):
		if s[i] != t[i]:
			return s[i+1:] == t[i:]
	return True
else:
	cnt = 0
	for i in range(len(s)):
		if s[i] != t[i]:
			cnt += 1
	return cnt == 1
