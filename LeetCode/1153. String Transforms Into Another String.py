"""
1153.String Transforms Into Another String
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into 
str2 
by doing zero or more conversions.
In one conversion you can convert all occurrences of one character in str1 to any other lowercase 
English character.
Return true if and only if you can transform str1 into str2.
"""

#hashmap

class Solution:
	def canConvert(self, str1: str, str2: str) -> bool:
		m = {}
		set2 = set()
		for i in range(len(str1)):
			set2.add(str2[i])
			if str1[i] in m and m[str1[i]] != str2[i]: return False
			m[str1[i]] = str2[i]
		if str1 != str2 and len(m) == 26 and len(set2) == 26: return False
		else: return True

