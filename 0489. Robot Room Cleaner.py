"""
489.Robot Room Cleaner
Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
"""

#dfs+backtracking

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def cleanRoom(robot):
    visited = set()
    dfs(robot, 0, 0, 0, visited)

def dfs(robot, r, c, dirr, visited)
        robot.clean()
        visited.add((r, c))
        for i in range(4):
            cur_dir = (i+dirr)%4
            r_next = r+dirs[cur_dir][0]
            c_next = c+dirs[cur_dir][1]
            if (r_next, c_next) not in visited and robot.move():
                dfs(robot, r_next, c_next, cur_dir, visited)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnRight()
