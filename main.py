import GlobalConstants
#import PrintSnake
import Snake

def main():
    snakes = [Snake.SnakeAI() for i in range(GlobalConstants.N)]
    GENERATION = 1

    while True:
        time_max = 100 # GlobalConstants.T(GENERATION)
        fitness = []

        for s in snakes:
            fit = sum([Snake.SnakeSimulation(s, time_max).Fitness for _ in range(5)])
            fitness.append((fit / 5, s))

        fitness.sort()
        fitness = fitness[::-1]

        if GENERATION % 2 == 0:
           print("Best fitness is  ", fitness[0][0])

        new_snakes = []
        for i in snakes[:GlobalConstants.SURVIVAL]:
            new_snakes.append(i)
            for _ in range(9):
                new_snakes.append(i.Evolve(1))

        snakes = new_snakes
    
        GENERATION += 1




if __name__ == "__main__":
    main()
