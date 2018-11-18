import matplotlib.pyplot as plt
from Sample_dB_converter import SamplesConverter
from scipy import signal
import numpy as np


class Plotter:

    def simple_plot(self, data):
        print('i want to plot something')
        plt.plot(data)
        plt.show()

