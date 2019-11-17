"""
1088. Confusing Number II
We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)
Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
"""

#dfs

class Solution:
	def confusingNumberII(self, N:int) -> int:
		self.res = 0
		self.dfs(N, 0)
		return self.res

	def dfs(self, N, cur_num):
		if cur_num > N: return
		if cur_num != 0:
			if self.isConfusing(cur_num): self.res += 1
			self.dfs(N, cur_num*10)
		self.dfs(N, cur_num*10+1)
		self.dfs(N, cur_num*10+6)
		self.dfs(N, cur_num*10+8)
		self.dfs(N, cur_num*10+9)

	def isConfusing(self, cur_num) -> bool:
		rotated = self.getRotated(cur_num)
		if rotated == None: return False
		if rotated != cur_num: return True
		else: return False

	def getRotated(self, cur_num) -> int:
		cur_str = str(cur_num)
		rotated = ''
		for i in range(len(cur_str)-1, -1, -1):
			c = cur_str[i]
			if c in ('0', '1', '6', '8', '9'):
				if c == '6':
					rotated += '9'
				elif c == '9':
					rotated += '6'
				else: rotated += c
			else: return None
		return int(rotated)