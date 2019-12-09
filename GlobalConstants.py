import math

# Terrain constants

N           = 1000
SURVIVAL    = 100
DIM         = 10 
KIDS = N / SURVIVAL

def T(GEN : int):
    return 100 * (1 + GEN / 100)


# Fitness constants 

COEF_FOOD = 0.3
COEF_TIME = 0.5
COEF_FREE = 0.2

def TOTAL_FITNESS(FOOD_FITNESS : float, TIME_FITNESS : float, FREE_FITNESS : float):
    return COEF_FOOD * FOOD_FITNESS + \
           COEF_TIME * TIME_FITNESS + \
           COEF_FREE * FREE_FITNESS


# Evolution constants:

    
def Coeficient(i : int, GENERATION : int):
    return (i / KIDS) * math.pow(10, -math.log(GENERATION) / 2 + 1)