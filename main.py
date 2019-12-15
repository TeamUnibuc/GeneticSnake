import GlobalConstants
#import PrintSnake
import Snake
import copy
import numpy as np

def main():
    snakes = [Snake.SnakeAI() for i in range(GlobalConstants.N)]
    GENERATION = 1

    while True:
        print("New generation ...")
        time_max = 100 # GlobalConstants.T(GENERATION)
        fitness = []

        for s in snakes:
            fit = Snake.SnakeSimulation(s, time_max).Fitness
            fitness.append((fit, s))

        fitness.sort()
        fitness = fitness[::-1]

        print("Best fitness is  ", fitness[0][0])

        new_snakes = []
        for i in fitness[:GlobalConstants.SURVIVAL]:
            new_snakes.append(i[1])
            new_snakes.append(copy.deepcopy(i[1]))
            new_snakes[-1].Evolve(1e-4)

        ord = [(i + j, (i, j)) for j in range(len(new_snakes)) \
             for i in range(j, len(new_snakes))]

        ord = sorted(ord)

        for i in ord:
            if len(new_snakes) == len(snakes):
                break
            a, b = i[1]
            if max(a, b) >= len(snakes):
                continue
            new_snakes.append(Snake.Evolve(snakes[a], snakes[b]))

        snakes = new_snakes
    
        GENERATION += 1




if __name__ == "__main__":
    main()
