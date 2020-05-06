# 721. Accounts Merge

# Graph dfs


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_accounts = [False] * len(accounts)
        g = collections.defaultdict(list)
        res = []

        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                g[email].append(i)

        # DFS code for traversing accounts.
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in g[email]:
                    dfs(neighbor, emails)

        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
