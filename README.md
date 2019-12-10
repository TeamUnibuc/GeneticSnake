# ML
Snake AI

# Arhitecture:
# Input:
    1. position X of head
    2. position Y of head
    3. position DX of food from head
    4. position DY of food from head
    5. distance to wall/tail down
    6. distance to wall/tail right
    7. distance to wall/tail up
    8. distance to wall/tail left

# Output:
    1. probability of going down
    2. probability of going right
    3. probability of going up
    4. probability of going left

# Decision:
    Making the snake making one step towards the dominant decision from Output

# Processing:
    N           = 1000
    SURVIVAL    = 100
    T           = 100 * (1 + GEN / 100)
    DIM         = 10 
    
    Each generation has N individuals, playing on a DIM x DIM matrix, and having at most T time stamps to make the biggest fitness.

    After each generation, the best SURVIVAL snakes evolve in N / SURVIVAL new snakes.

# Fitness:

    FOOD_FITNESS = food eaten
    TIME_FITNESS = time alive
    CLOSE_FITNESS = average of # of steps towards food

    TOTAL_FITNESS = FOOD_FITNESS + TIME_FITNESS + CLOSE_FITNESS

# Evolution:
    Each individual evolves into N / SURVIVAL new individuals.
    The evolution process from snake S is:

    G = generation
    NR = N / SURVIVAL
    S_i = S + (RandomWeights * (i / NR) * 10^(-ln(G) - 1))