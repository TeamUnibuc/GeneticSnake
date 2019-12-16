import GlobalConstants
#import PrintSnake
import Snake
import copy
import numpy as np
import random
import PrintSnake

def main():
    snakes = [Snake.SnakeAI() for i in range(GlobalConstants.N)]
    GENERATION = 1

    last = 0

    while True:
        print("New generation ...")
        time_max = 1000 # GlobalConstants.T(GENERATION)
        fitness = []

        for sn in snakes:
            s = Snake.SnakeSimulation(sn, time_max)
            fit = s.Fitness
            if random.randint(1, 100) == 1:
                print("Made ", s.alive_time, " moves, of which ", s.avg, " where towards the food, and ate ", s.eaten, " times")
            
            if s.eaten > last:
                last = s.eaten
                PrintSnake.PrintSnake(s.vizual)

            fitness.append((fit, sn))

        fitness.sort()
        fitness = fitness[::-1]

        print("Best fitness is  ", fitness[0][0])

        new_snakes = []
        for i in fitness[:GlobalConstants.SURVIVAL]:
            new_snakes.append(i[1])
            new_snakes.append(copy.deepcopy(i[1]))
            new_snakes[-1].Evolve()
            new_snakes.append(copy.deepcopy(i[1]))
            new_snakes[-1].Evolve()

        ord = [(i + j, (i, j)) for j in range(len(new_snakes)) \
             for i in range(j, len(new_snakes))]

        random.shuffle(ord)

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
