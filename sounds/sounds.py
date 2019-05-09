import numpy as np
import matplotlib.pyplot as plt

fs = 44100


def clean(frequency, duration):
    wave = np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)
    return wave.astype(np.float32)


def plot(wave):
    x = np.arange(fs)
    plt.plot(x, wave)
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.show()
