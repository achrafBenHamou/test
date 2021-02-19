import numpy as np
from scipy import signal


def synchronize(list_a: list, list_b: list) -> tuple:
    """
    This function find the delay between the two given signals.
    Once the delay computed, it synchronize them and crop the signals
    in order to have the same signals lenght.

    :param list_a: unsynchronized signal a in list
    :param list_b: unsynchronized signal b in list
    :return: list_a and list_b synchronized
    """
    pass


if __name__ == "__main__":
    A = [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3]
    B = [1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1]

    synced_A, synced_B = synchronize(A, B)

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(2, 1)
    ax[0].set_title("Original signals")
    ax[0].plot(A, "o-", label="signal A", markersize=8)
    ax[0].plot(B, "*-", label="signal B")
    ax[0].legend()
    ax[1].set_title("Synced signals")
    ax[1].plot(synced_A, "o-", label="signal A", markersize=8)
    ax[1].plot(synced_B, "*-", label="signal B")
    ax[1].legend()
    plt.show()