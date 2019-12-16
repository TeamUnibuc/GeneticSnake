import GlobalConstants
import torch as th
import random
import copy

class SnakeAI:
    def __lt__(self, oth):
        return random.randint(1, 2) == 1

    def __init__(self):
        lvl1 = GlobalConstants.IN_FEATURES
        lvl2 = 10
        lvl3 = GlobalConstants.OUT_FEATURES

        self.layers = [th.randn(lvl1, lvl2), th.randn(lvl2, lvl3)]

    def Act(self, v):
        v = th.tensor(v, dtype=th.float).reshape((1, -1))
        
        for i in self.layers:
            v = v.mm(i)
            #v = th.max(th.tensor([0.]), v)
        
        v = v.reshape((-1)).tolist()

        return v.index(max(v))

    def Evolve(self, coef : float):
        for i in self.layers:
            for j in i:
                j += th.randn(j.shape) * coef

def Evolve(a : SnakeAI, b : SnakeAI):
    if random.randint(1, 2) == 1:
        a, b = b, a

    c = copy.deepcopy(a)
    for q in range(len(c.layers)):
        n = random.randint(0, c.layers[q].shape[0])
        m = random.randint(0, c.layers[q].shape[1])
        for i in range(c.layers[q].shape[0]):
            for j in range(c.layers[q].shape[1]):
                if i > n or (i == n and j > m):
                    c.layers[q][i][j] = b.layers[q][i][j]
    return c

class SnakeSimulation:
    def RandomPoz(self):
        while True:
            x = random.randint(0, self.DIM - 1)
            y = random.randint(0, self.DIM - 1)
            if self.matrix[x][y] == 0:
                return (x, y)

    def distance(self, x, y, dx, dy):
        x += dx
        y += dy
        ans = 0
        while True:
            if min(x, y) < 0 or max(x, y) >= self.DIM or self.matrix[x][y] == 1:
                return ans
            ans += 1
            x += dx
            y += dy

    def See(self):
        x, y = self.pozition[-1]
        v = []
        v += [x - self.Food[0], y - self.Food[1]] # position of food
        v += [self.distance(x, y, 1, 0)]
        v += [self.distance(x, y, 0, 1)]
        v += [self.distance(x, y, -1, 0)]
        v += [self.distance(x, y, 0, -1)]
        return v

    def NewPoz(self):
        see = self.See()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]][self.snakeai.Act(see)]
        direction[0] += self.pozition[-1][0]
        direction[1] += self.pozition[-1][1]
        
        if min(direction) < 0 or max(direction) >= self.DIM or \
                self.matrix[direction[0]][direction[1]] == 1:
            self.lost = 1
            return

        if direction[0] == self.Food[0] and direction[1] == self.Food[1]:
            self.eaten += 1
            #self.Food = self.RandomPoz()
        else:
            self.matrix[self.pozition[0][0]][self.pozition[0][1]] = 0
            self.pozition = self.pozition[1:]
        self.pozition.append(direction)
        self.matrix[direction[0]][direction[1]] = 1

    def __init__(self, snakeai : SnakeAI, time : int):
        self.snakeai = snakeai
        self.DIM = GlobalConstants.DIM
        self.pozition = [[self.DIM // 2, self.DIM // 2]]
        self.matrix = [[0 for i in range(self.DIM)] for j in range(self.DIM)]
        self.matrix[self.pozition[0][0]][self.pozition[0][1]] = 1
        self.Food = self.RandomPoz()
        self.lost = 0
        self.eaten = 0

        alive_time = 0
        avg = 0.

        while alive_time < time and self.lost == 0:
            alive_time += 1
            dinit = abs(self.pozition[-1][0] - self.Food[0]) + abs(self.pozition[-1][1] - self.Food[1])
            self.NewPoz()
            dfinal = abs(self.pozition[-1][0] - self.Food[0]) + abs(self.pozition[-1][1] - self.Food[1])
            avg += int(dfinal < dinit)
        
        self.alive_time = alive_time
        self.avg = avg
        self.Fitness = self.alive_time + self.eaten + avg / alive_time
