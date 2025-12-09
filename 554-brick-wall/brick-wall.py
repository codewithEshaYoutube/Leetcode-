class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gaps={0:0}  # mapping of positions and count of gaps
        for r in wall:
            total=0
            for b in r[:-1]:
                total+=b
                count_gaps[total]=1+count_gaps.get(total,0)
        return len(wall)-(max(count_gaps.values()) if count_gaps else 0)