import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt


ON = 255
OFF = 0
vals = [ON, OFF]
pos = 0.035


def random_grid(N):
    return np.random.choice(vals, N*N, p=[pos, 1-pos]).reshape(N, N)


def update(unknown, img, grid, N):

    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                         grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255)

            if grid[i, j] == ON:
                if (total < 2) or (total >4):
                    new_grid[i, j] = OFF
            else:
                if (total == 3) or (total == 4):
                    new_grid[i, j] = ON

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


def main():
    N = 100
    update_interval = 50

    grid = random_grid(N)

    # set up a animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    display = ani.FuncAnimation(fig, update, frames=10,
                                fargs=(img, grid, N),
                                interval=update_interval,
                                save_count=50)

    plt.show()


if __name__ == '__main__':
    main()