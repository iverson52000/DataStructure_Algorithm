"""
299. Bulls and Cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask 
your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that 
indicates how many digits in said guess match your secret number exactly in both digit and position 
(called "bulls") and how many digits match the secret number but locate in the wrong position 
(called "cows"). Your friend will use successive guesses and hints to eventually derive the secret 
number.
Write a function to return a hint according to the secret number and friend's guess, use A to indicate 
he bulls and B to indicate the cows. 
Please note that both secret number and friend's guess may contain duplicate digits.
"""

#hashmap

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        m = {str(k):0 for k in range(0,10)}
        A = 0; B = 0    
        for i in range(len(secret)):
            if secret[i] == guess[i]: A += 1
            else:
                if m[secret[i]] < 0: B += 1
                m[secret[i]] += 1
                if m[guess[i]] > 0: B += 1
                m[guess[i]] -= 1  
        return str(A)+'A'+str(B)+'B'
