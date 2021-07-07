"""
340. Longest Substring with At Most K Distinct Characters
Given a string, find the length of the longest substring T that contains at most k distinct characters.
For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.
"""

#hashmap+two pointer

class LongestSub:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		res = 0
		left = 0
		m = {}
		for i in range(len(s)):
			m[s[i]] = m.get(s[i], 0)+1
			while len(m) > K:
				m[s[left]] -= 1
				if m[s[left]] == 0: m.pop(s[left])
				left += 1
			res = max(res, i-left+1)
		return res
