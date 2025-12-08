class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counter_gap={}
        for r in wall:
            total=0
            for b in r[:-1]:
                total+=b
                counter_gap[total]=1 + counter_gap.get(total,0)
        return len(wall)-(max(counter_gap.values()) if counter_gap else 0  ) 
        