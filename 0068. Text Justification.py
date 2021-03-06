"""
68. Text Justification
Given an array of words and a width maxWidth, format the text such that each line has exactly 
maxWidthcharacters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each 
line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces 
on a line do not divide evenly between words, the empty slots on the left will be assigned more 
spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between 
words.
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for word in words:
            if num_of_letters+len(word)+len(cur) > maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [word]
            num_of_letters += len(word)
        return res+[' '.join(cur).ljust(maxWidth)]
