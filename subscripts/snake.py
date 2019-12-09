import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib
import time

def PrintSnake(dim : (int, int), food : (int, int), snake : list):
    N, M = dim
    img = [[[0, 0, 0] for i in range(N)] for j in range(M)]
    img[food[0]][food[1]] = [255, 0, 0]

    for i in range(len(snake)):
        cst = int(255 * (0.5 + 0.5 * i / len(snake)))
        img[snake[i][0]][snake[i][1]] = [cst, cst, cst]

    return img

def urm(a, b, dx, dy, N, M):
    if a + dx >= 0 and a + dx < N and b + dy >= 0 and b + dy < M:
        return (a + dx, b + dy, dx, dy)
    dx, dy = -dy, dx
    return urm(a, b, dx, dy, N, M)
    
def show_path(N, M):
    global img
    food = (1, 1)
    snake = [(0, 0)]
    a, b, dx, dy = 0, 0, 1, 0


    for _ in range(15):
        img.append(PrintSnake((N, M), food, snake))
        (a, b, dx, dy) = urm(a, b, dx, dy, N, M)
        snake.append((a, b))
        time.sleep(0.1)

#plt.ion()
fig = plt.figure()

ims, img = [], []

show_path(10, 10)

for i in img:
    im = plt.imshow(i, animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, repeat=True)

plt.show()

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)


