"""
809. Expressive Words
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> 
"hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same: 
 "h", "eee", "ll", "ooo".
For some given string S, a query word is stretchy if it can be made to be equal to S by any number of 
applications of the following extension operation: choose a group consisting of characters c, and add 
some number of characters c to the group so that the size of the group is 3 or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we 
cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
Given a list of query words, return the number of words that are stretchy.
"""

#Two pointer+Traverse

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i_word = 0
            valid = True
            for i_S in range(len(S)):
                if i_word < len(word) and S[i_S] == word[i_word]: i_word += 1
                elif S[i_S-1:i_S+2] != S[i_S]*3 != S[i_S-2:i_S+1]:
                    valid = False
                    break
            if valid and i_word == len(word): res += 1
        return res

