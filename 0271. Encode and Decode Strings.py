"""
271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent 
over the network and is decoded back to the original list of strings.
"""

strs = ["123abc", "xyz"]

def encode(self, strs):
    encoded = ''
    for s in strs:
    	encoded += str(len(s))+'/'+s
    return encoded
  
s = '6/123abc3/xyz'

def decode(self, s):
    res = []
    i = 0
    while i < len(s):
        i_slash = s.find('/', i)
        i = i_slash+1+int(s[i:i_slash])
        res.append(s[i_slash+1:i])
    return res
