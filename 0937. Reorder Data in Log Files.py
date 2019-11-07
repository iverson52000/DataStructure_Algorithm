"""
937. Reorder Data in Log Files
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:
•	Each word after the identifier will consist only of lowercase letters, or;
•	Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each 
log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log. The letter-logs are 
ordered lexicographically ignoring identifier, with the identifier used in case of ties. The digit-logs should be put in their original order.

Return the final order of the logs.
"""

#sort

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []          
        for log in logs:
            if log.split()[1].isdigit(): digit_logs.append(log)
            else: letter_logs.append(log)
                
        letter_logs.sort(key=lambda log: log.split()[0])     # when suffix is tie, sort by identifier
        letter_logs.sort(key=lambda log: log.split()[1:])    # sorted by suffix
        
        return letter_logs+digit_logs    # put digit logs after letter logs