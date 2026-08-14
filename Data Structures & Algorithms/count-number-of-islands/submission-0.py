from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        count=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=="1":
                    q.append([x,y])
                    while(q):
                        vx,vy=q.popleft()
                        for dx,dy in directions:
                            cx,cy=vx+dx,vy+dy
                            if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and grid[cx][cy] == "1":
                                grid[cx][cy]="0"
                                q.append([cx,cy])
                    count+=1
        return count