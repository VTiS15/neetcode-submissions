class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        n = len(candidates)
        res = []

        def dp(idx: int = 0, total: int = 0, chosen: List[int] = []):
            if total == target:
                res.append(chosen.copy())
                return
            if total > target or idx == n:
                return

            chosen.append(candidates[idx])
            dp(idx + 1, total + candidates[idx], chosen)
            chosen.pop()

            while idx + 1 < n and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dp(idx + 1, total, chosen)
    
        dp()
        return res
        