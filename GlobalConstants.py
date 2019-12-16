import math

# Terrain constants

IN_FEATURES     = 6
OUT_FEATURES    = 4

N               = 100
SURVIVAL        = 10
DIM             = 10

def T(GEN : int):
    return 100 * (1 + GEN / 100)

# Evolution constants:
    
def Coeficient(id : int, GENERATION : int):
    return (id / KIDS) * math.pow(10, -math.log(GENERATION) / 2 + 1)