import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib
import time
import GlobalConstants

def PrintSnakeFrame(food : (int, int), snake : list):
    N = M = GlobalConstants.DIM
    
    img = [[[0, 0, 0] for i in range(N)] for j in range(M)]
    img[food[0]][food[1]][0] = 255

    for i in range(len(snake)):        
        cst = int(255 * (0.5 + 0.5 * i / len(snake)))
        img[snake[i][0]][snake[i][1]] = [cst] * 3

    return img

def PrintSnake(snake : list):
    img = []
    for i in snake:
        img.append(PrintSnakeFrame(i[1], i[0]))

    #plt.ion()
    fig = plt.figure()
    frames = []
    
    for i in img:
        im = plt.imshow(i, animated=True)
        frames.append([im])

    ani = animation.ArtistAnimation(fig, frames, repeat=False)
    ani.save("Fig.mp4")
    #plt.show()


# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)


