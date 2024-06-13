import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_animation(time_data, ubar_data,xlim_inf,xlim_sup, coord_y,Title,labelX,labelY, output_file='animation.gif'):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'b-')
    
    ax.set_xlim(xlim_inf,xlim_sup)
    ax.set_ylim(np.nanmin(coord_y), np.nanmax(coord_y))
    
    ax.set_xlabel(labelX)
    ax.set_ylabel(labelY)
    ax.set_title(Title)
    ax.grid()
    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        y = coord_y
        ubar = ubar_data[:, frame]
        line.set_data(ubar, y)
        ax.set_title(f'{Title} (Temps = {time_data[frame]:.2f})')
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(time_data), init_func=init, blit=True)
    ani.save(output_file, writer='ffmpeg', fps=15 )


def create_animation_dual(time_data, ubar_data1, ubar_data2,xlim_inf,xlim_sup, coord_y, Title, labelX, labelY, label1, label2,output_file='animation_dual.gif'):
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], 'b-', label=label1)
    line2, = ax.plot([], [], 'r-', label=label2)
    
    ax.set_xlim(xlim_inf,xlim_sup)
    ax.set_ylim(np.min(coord_y), np.max(coord_y))
    
    ax.set_xlabel(labelX)
    ax.set_ylabel(labelY)
    ax.set_title(Title)
    ax.grid()
    ax.legend()
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2

    def update(frame):
        y = coord_y
        ubar1 = ubar_data1[:, frame]
        ubar2 = ubar_data2[:, frame]
        line1.set_data(ubar1, y)
        line2.set_data(ubar2, y)
        ax.set_title(f'{Title} (Temps = {time_data[frame]:.2f})')
        return line1, line2

    ani = animation.FuncAnimation(fig, update, frames=len(time_data), init_func=init, blit=True)
    ani.save(output_file, writer='ffmpeg', fps=15)

