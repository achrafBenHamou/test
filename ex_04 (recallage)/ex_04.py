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
    def apply(x, y):
        return x - y

    from itertools import groupby
    # are_equal verifie if all elements of iterable are equal
    def are_equal(iterable):
        e = groupby(iterable)
        return next(e, True) and not next(e, False)

    # size of the smallest list
    min_length = min (len(list_a),len(list_b))
    i = 0
    t = []
    while i <= min_length :
        o1 = map(apply, list_a[i:], list_b)
        o2 = map(apply, list_a, list_b[i:])

        l1 = list(o1)
        l2 = list(o2)

        if are_equal(l1[:len(l1)-i]) :
            t.append([len(l1[:len(l1)]),i,1])
        if are_equal(l2[:len(l2)-i]):
            t.append([len(l2[:len(l2)]), i, 2])
        i+=1

    if max(t)[2] == 1 :
        A_list = list_a[max(t)[1]:max(t)[0]+max(t)[1]]
        B_list = list_b[:max(t)[0] - max(t)[1]+max(t)[1]]
        return (A_list, B_list)
    else :
        A_list = list_a[:max(t)[0] - max(t)[1]+max(t)[1]]
        B_list = list_b[max(t)[1]:max(t)[0]+max(t)[1]]
        return (A_list, B_list)


if __name__ == "__main__":
    A = [0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2]
    B = [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3]
    #print(synchronize(A, B))
    synced_A, synced_B = synchronize(B, A)
    #print(synced_A)
    #print(synced_B)
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