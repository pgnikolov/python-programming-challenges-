class Robot:
    def __init__(self, index, position, health, direction):
        self.index = index
        self.position = position
        self.health = health
        self.direction = direction


class Solution:
    def survivedrobotshealths(self, positions, healths, directions):
        robots = [Robot(index, pos, health, dir) for index, (pos, health, dir) in
                  enumerate(zip(positions, healths, directions))]
        robots.sort(key=lambda robot: robot.position)

        stack = []
        for robot in robots:
            if robot.direction == 'R':
                stack.append(robot)
                continue
            while stack and stack[-1].direction == 'R' and robot.health > 0:
                if stack[-1].health == robot.health:
                    stack.pop()
                    robot.health = 0
                elif stack[-1].health < robot.health:
                    stack.pop()
                    robot.health -= 1
                else:
                    stack[-1].health -= 1
                    robot.health = 0

            if robot.health > 0:
                stack.append(robot)

        stack.sort(key=lambda robot: robot.index)
        return [robot.health for robot in stack]
