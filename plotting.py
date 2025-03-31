
from matplotlib import pyplot as plt
from matplotlib import cm


def plot(JL, AM, AM2, title): # Plotting Function - Plot and display the three images with labels
    fig, axes = plt.subplots(1, 3)
    ax = axes.ravel()
    fig.suptitle(title, fontsize=18, y=0.75)
    ax[0].set_title('10905 JL.bmp')
    ax[0].imshow(JL, cmap=cm.gray)
    ax[0].set_axis_off()

    ax[1].set_title('43590 AM.bmp')
    ax[1].imshow(AM, cmap=cm.gray)
    ax[1].set_axis_off()

    ax[2].set_title('9343 AM.bmp')
    ax[2].imshow(AM2, cmap=cm.gray)
    ax[2].set_axis_off()

    plt.tight_layout()
    plt.show()#block=False)
    plt.close(fig)
   