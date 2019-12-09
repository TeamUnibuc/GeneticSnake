import torch as th
import GlobalConstants
import PrintSnake
import Model
import Simulator

def main():
    snakes = [Model.GetRandomSnake() for i in range(GlobalConstants.N)]
    GENERATION = 1

    while True:
        fitness = []

        for s in snakes:
            fit = Simulator.Fitness(s)
            fitness.append((fit, s))

        fitness.sort()

        print("Generation 1 completed\n")
        Simulator.Show(fitness[0][1])

        new_snakes = []
        for i in snakes[:GlobalConstants.SURVIVAL]:
            new_snakes += Model.evolve(i, GENERATION)

        snakes = new_snakes

        GENERATION += 1




if __name__ == "__main__":
    main()
