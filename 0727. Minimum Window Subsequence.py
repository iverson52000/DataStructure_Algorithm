"""
!727.Minimum Window Subsequence
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
If there is no such window in S that covers all characters in T, return the empty string "". 
If there are multiple such minimum-length windows, return the one with the left-most starting index.
"""

#Two pointers

S = "abcdebdde"; T = "bde"
#Output: "bcde"

res = ''
i_T = 0; minn = len(S)+1

for i_S in range(len(S)):
	if S[i_S] == T[i_T]: i_T += 1
		if i_T >= len(T):
			end = i_S+1
			i_T -= 1
			while i_T >= 0:
				if S[i_S] == T[i_T]: i_T -= 1
				i_S -= 1
			i_T += 1; i_S += 1
			if end-i_S < minn:
				minn = end-i_S
				res = S[i_S:i_S+end-1]






