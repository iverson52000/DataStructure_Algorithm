m = collections.defaultdict(int)
for transaction in transactions:
    m[transaction[0]] += transaction[2]
    m[transaction[1]] -= transaction[2]

balances = []
for val in m.values():
    if val != 0: balances.append(val)

res = dfs(0, balances)

def dfs(level, balances) -> int:
    if level == len(balances): return 0
    cur_num = balances[level]
    if cur_num == 0: return dfs(level+1, balances)
    minn = flaot('inf')
    for i in range(level+1, len(balances)):
        nxt = balances[i]
        if cur*nxt < 0:
            balances[i] = cur+nxt
            minn = min(minn, 1+dfs(i))
