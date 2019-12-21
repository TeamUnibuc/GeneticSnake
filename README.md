# Snake AI

An AI based on a genetic evolutionary algorithm, that learns how to play snake on a 10x10 matrix.
For visualizing the AI, the best snake overall (number of eaten snaks) is captured in an mp4 file called "Fig.mp4"

![sample snake](https://github.com/TeamUnibuc/GeneticSnake/blob/master/Samples/sample.png)

# Arhitecture:
## Input:
    1. Xfood - Xhead
    2. Xhead - Xfood
    3. Yfood - Yhead
    4. Yhead - Yfood
    5. distance to wall/tail down
    6. distance to wall/tail right
    7. distance to wall/tail up
    8. distance to wall/tail left

## Output:
    1. probability of going down
    2. probability of going right
    3. probability of going up
    4. probability of going left

## Decision:
    Making the snake making one step towards the dominant decision from Output

## Processing:
    The exact value for the constants is given in the file 'GlobalConstants.py'.

    Each generation has N individuals, playing on a DIM x DIM matrix, and having at most T time stamps without eating to make the biggest fitness.

    After each generation, the best SURVIVAL snakes evolve in N / SURVIVAL new snakes.

## Fitness:
    The fitness of a snake is the number of times it ate.

## Evolution:
    Each individual evolves into N / SURVIVAL new individuals.
    The evolution process is the following:
    1. Each snake breakes down into 2 copies: one identical and one with some minor mutations.
    2. Pairs of snakes cross-bread: one new snake is made with a part of the ADN of the first snake and a part of the second one, WITHOUT mutations.
